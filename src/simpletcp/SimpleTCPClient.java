package simpletcp;

import java.io.*;
import java.net.*;

class SimpleTCPClient {
	public static void main(String argv[]) throws IOException {
		String sentence;
		String modifiedSentence;
		System.out.println("Mensagem: ");

		BufferedReader inFromUser = new BufferedReader(new InputStreamReader(System.in));
		Socket clientSocket;
		sentence = inFromUser.readLine();

		try {
			clientSocket = new Socket("localhost", 6789);
			DataOutputStream outToServer = new DataOutputStream(clientSocket.getOutputStream());
			BufferedReader inFromServer = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));

			outToServer.writeBytes(sentence + "\n");
			outToServer.flush();
			modifiedSentence = inFromServer.readLine();
			System.out.println("FROM SERVER: " + modifiedSentence);
			clientSocket.close();
		} catch (IOException e) {
			e.printStackTrace();
		}
	}
}