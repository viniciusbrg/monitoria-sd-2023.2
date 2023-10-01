package serialization;

import java.io.*;
import java.net.*;

class SerializationSimpleTCPClient {
	public static void main(String argv[]) {

		Pessoa p1 = new Pessoa("Joao da Silva", "Quixada", 999881122, 2012);
		
		System.out.println("serialization.Pessoa p1: " + p1.toString());
		Socket clientSocket;
		try {
			clientSocket = new Socket("localhost", 6789);
			ObjectOutputStream outToServer = new ObjectOutputStream(clientSocket.getOutputStream());
			ObjectInputStream inFromServer = new ObjectInputStream(clientSocket.getInputStream());
			outToServer.writeObject(p1);
			Pessoa p2 = (Pessoa) inFromServer.readObject();
			System.out.println("serialization.Pessoa p2: " + p2.toString());
			clientSocket.close();
		} catch (IOException e) {
			e.printStackTrace();
		} catch (ClassNotFoundException e) {
			e.printStackTrace();
		}
	}
}