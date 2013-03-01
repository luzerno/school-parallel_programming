public class CoinFlip {
    private static int numThreads;
    private static long numIterations;
    private static CoinThread[] coinThreads;
    private static Thread[] threads;
    private static long startTime, endTime;
    
    
    private static void flip() {
    	startTime = System.currentTimeMillis();
    	for (int i = 0; i < numThreads; i++) {
    		threads[i].start();
    	}
    	
    	for (int i = 0; i < numThreads; i++) {
    		try {
    			threads[i].join();
    		} catch (InterruptedException e) {
    			System.err.println("Thread interrupted");
    		}
    	}
    	endTime = System.currentTimeMillis();
    }
    private static void collectResults() {
    	long numHeads = 0;
    	for (int i = 0; i < numThreads; i++) {
    		numHeads += coinThreads[i].getNumHead();
    		System.out.println("Thread #" + coinThreads[i].getThreadId() + ": " + coinThreads[i].getNumHead() + " heads in " + coinThreads[i].getNumIterations() + " tosses.");
    	}
    	System.out.println(numHeads + " heads in " + numIterations + " coin tosses.");
    	System.out.println("Elaspsed time: " + (endTime - startTime) + "ms");
    	
    }
    private static void initCoinThreads() {
    	long numIterationsPerThread = numIterations / numThreads;
    	long numRemainIterations = numIterations % numThreads;
    	coinThreads = new CoinThread[numThreads];
    	threads = new Thread[numThreads];
    	for (int i = 0; i < numThreads; i++) {
    		long num = numIterationsPerThread;
    		if (numRemainIterations > 0) {
    			num++;
    			numRemainIterations--;
    		}
    		coinThreads[i] = new CoinThread(i, num);
    		threads[i] = new Thread(coinThreads[i]);
    	}
    }
    
    private static void parseArgs(String[] args) {
        int size = args.length;  
        if (size != 2) {
            System.err.print("Usage: CoinFlip #threads #iterations\n");
            System.exit(0);
        }
        try {
            numThreads = Integer.parseInt(args[0]);
            numIterations = Long.parseLong(args[1]);
        } catch (NumberFormatException e) {
            System.err.print("Usage: CoinFlip #threads #iterations\n");
        }
    }
    
    public static void main(String[] args) {
        parseArgs(args);
        initCoinThreads();
        flip();
        collectResults();
    }
}

