package serialization;

import java.io.*;
import java.net.*;

class SerializationSimpleTCPServer {
	public static void main(String argv[]) {
		ServerSocket listenSocket;
		try {
			System.out.println("Running server");

			listenSocket = new ServerSocket(6789);
			while (true) {
				Socket connectionSocket = listenSocket.accept();
				ObjectOutputStream outToClient = new ObjectOutputStream(connectionSocket.getOutputStream());
				ObjectInputStream inFromClient = new ObjectInputStream(connectionSocket.getInputStream());
				Pessoa p = (Pessoa) inFromClient.readObject();

				System.out.println("Mensagem do tipo pessoa recebida!");
				System.out.println(p.toString());

				p.cidade = "Fortaleza";
				p.ano = 2014;
				outToClient.writeObject(p);
			}
		} catch (IOException e) {
			e.printStackTrace();
		} catch (ClassNotFoundException e) {
			e.printStackTrace();
		}

	}
}