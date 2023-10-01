package simpletcp;

import java.io.*;
import java.net.*;
import java.nio.Buffer;

class SimpleTCPServer {
	public static void main(String argv[]) {
		String clientSentence;
		String capitalizedSentence;
		ServerSocket listenSocket;
		try {
			listenSocket = new ServerSocket(6789);

			System.out.println("Waiting for new messages");

			while (true) {
				Socket connectionSocket = listenSocket.accept();
				BufferedReader inFromClient = new BufferedReader(
						new InputStreamReader(new BufferedInputStream(connectionSocket.getInputStream()))
				);
				DataOutputStream outToClient = new DataOutputStream(connectionSocket.getOutputStream());

				clientSentence = inFromClient.readLine();

				System.out.println("Got message from client: " + clientSentence);

				capitalizedSentence = new StringBuilder(clientSentence.toUpperCase()).reverse().toString() + '\n';
				outToClient.writeBytes(capitalizedSentence);
				outToClient.flush();
			}
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}

	}
}