import sys
import speedtest

def run_speedtest():
    """Run speed test and return results as a dictionary."""
    st = speedtest.Speedtest()

    #get best server
    best_server = st.get_best_server()
    print(f"Best server based on ping: {best_server['host']} located in {best_server['country']}")

    #download and upload tests in Mbps
    download_speed = st.download() / 1_000_000  
    upload_speed = st.upload() / 1_000_000      
    ping = st.results.ping

    return {
        "ping": round(ping, 2),
        "download": round(download_speed, 2),
        "upload": round(upload_speed, 2),
    }

def display_results(results):
    """Display the speedtest results nicely."""
    print("\n=== Internet Speed Test Results ===")
    print(f"Ping: {results['ping']} ms")
    print(f"Download Speed: {results['download']} Mbps")
    print(f"Upload Speed: {results['upload']} Mbps")
    print("===================================")

def main():
    try:
        results = run_speedtest()
        display_results(results)
    except Exception as e:
        print(f"Error during speed test: {e}")
        sys.exit(1)
    
    input("\nPress ENTER to exit...")

if __name__ == "__main__":
    main()
