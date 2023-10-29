package simpleudp;

import java.io.*;
import java.net.*;

class SimpleUDPServer {
	public static void main(String args[]) {
		DatagramSocket serverSocket = null;
		try {
			serverSocket = new DatagramSocket(6789);
			System.out.println("Servidor em execuçao!");
			byte[] receiveData = new byte[1024];
			int id = 0;
			while (true) {
				id++;
				System.out.println("Esperando Msg " + id + " ...");
				DatagramPacket request = new DatagramPacket(receiveData, receiveData.length);
				serverSocket.receive(request);

				String sentence = new String(request.getData(), 0, request.getLength());

				String clientAddress = request.getAddress().getHostAddress();
				int clientPort = request.getPort();

				System.out.println("Cliente: " + clientAddress + " - Porta: " + clientPort);
				System.out.println("Msg: " + sentence);

				String response = new StringBuilder(sentence.toUpperCase()).reverse().toString();
				byte[] responseBytes = response.getBytes();

				InetSocketAddress destinationAddress = new InetSocketAddress(clientAddress, clientPort);
				DatagramPacket sendPacket = new DatagramPacket(responseBytes, responseBytes.length, destinationAddress);
				serverSocket.send(sendPacket);
			}
		} catch (SocketException e) {
			e.printStackTrace();
		} catch (IOException e) {
			e.printStackTrace();
		} finally {
			if (serverSocket != null) serverSocket.close();
		}
	}
}