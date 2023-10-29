package simpleudp;

import java.io.*;
import java.net.*;

class SimpleUDPClient {
	public static void main(String args[]) {
		String ip = "localhost";
		String message = ">Socorram me subi no onibus em marrocoS";

		DatagramSocket clientSocket = null;
		try {
			clientSocket = new DatagramSocket(10000);
			byte[] sendArray = message.getBytes();
			InetAddress IpServidor = InetAddress.getByName(ip);
			int port = 6789;

			DatagramPacket sendPacket = new DatagramPacket(sendArray, sendArray.length, IpServidor, port);
			clientSocket.send(sendPacket);

			// modern syntax
			var responsePacket = new DatagramPacket(new byte[1024], 1024);
			clientSocket.receive(responsePacket);

			// check length because actual sent data might be smaller than 1024 bytes
			var parsedResponse = new String(responsePacket.getData(), 0, responsePacket.getLength());

			System.out.println("Sent message: \n" + message);
			System.out.println("Got response: \n" + parsedResponse);
		} catch (SocketException e) {
			e.printStackTrace();
		} catch (UnknownHostException e) {
			e.printStackTrace();
		} catch (IOException e) {
			e.printStackTrace();
		} finally {
			if (clientSocket != null) clientSocket.close();
		}
	}
}