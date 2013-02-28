public class DecryptThread implements Runnable {
	private SealedDES sealedDES;
	private int threadId;
	private long startKey, endKey;
	public DecryptThread(SealedDES sealedDES, int threadId, long startKey, long endKey) {
		this.sealedDES = sealedDES;
		this.threadId = threadId;
		this.startKey = startKey;
		this.endKey = endKey;
	}
	public int getThreadId() {
		return this.threadId;
	}
	public void run() {
		
	}
}
