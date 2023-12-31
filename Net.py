
import socket
import threading

HOST = '' #Listening to any 
PORT = 8000  # The port number of the server

exit_flag = threading.Event()  # Event for indicating when to exit


# Create a socket using IPv4 and TCP protocol
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    try:
        # Bind the socket to the specified IP address and port
        s.bind((HOST, PORT))

        # Listen for incoming connections
        s.listen(1)
        print(f"Server is listening on {HOST}:{PORT}")

        # Accept a client connection
        conn, addr = s.accept()
        print(f"Connected by {addr}")

        with conn:
            while not exit_flag.is_set():
                # Receive data from the client using ASCII encoding
                data = conn.recv(1024)
                if not data:
                    break

                decoded_data = data.decode('utf-8', errors='ignore')
                print(f'Received data from GPS Tracker: {decoded_data}')

                # Send the received data back to the client using ASCII encoding
                conn.sendall(data)

    except Exception as e:
        print(f"An error occurred: {e}")



print("Server has closed.")