import java.util.Random;

public class CoinThread implements Runnable {
    private int threadId;
    private long numIterations;
    private long numHead;
    private Random rand;
    public void run() {
    	for (long i = 0; i < numIterations; i++) {
    		if (rand.nextInt(2) == 1) {
    			this.numHead++;
    		}
    	}
    }
    public int getThreadId() {
    	return this.threadId;
    }
    public long getNumHead() {
    	return this.numHead;
    }
    public long getNumIterations() {
    	return this.numIterations;
    }
    public CoinThread(int threadId, long numIterations) {
        this.threadId = threadId;
        this.numIterations = numIterations;
        this.rand = new Random();
        this.numHead = 0;
//        System.out.println("Thread #" + this.threadId + " inited, get " + this.numIterations + " iterations.");
    }
}
