import java.io.IOException;
import java.util.Arrays;
import java.util.HashSet;
import java.util.Iterator;
import java.util.NoSuchElementException;
import java.util.Set;

import org.apache.commons.lang.ArrayUtils;
import org.apache.commons.lang.StringUtils;
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapred.OutputCollector;
import org.apache.hadoop.mapred.Reporter;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Reducer;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
import org.apache.hadoop.util.GenericOptionsParser;



public class fof {
	public static class FofMapper extends Mapper<LongWritable, Text, Text, Text> {
		public void map(LongWritable key, Text values, Context context) throws IOException, InterruptedException {
			System.out.println("I am mapper");
			String line = values.toString();
			String[] ppls = line.split(" ");
            String[] others;
            String me; 
            String frd;
            Text keyTuple = new Text();
            Text fList = new Text();

            me = ppls[0];
            for (int i = 1; i < ppls.length; i++) {
                frd = ppls[i];
                others = (String[]) ArrayUtils.addAll(Arrays.copyOfRange(ppls, 1, i), Arrays.copyOfRange(ppls, i + 1, ppls.length));

                if (Integer.parseInt(me) < Integer.parseInt(frd)) {
                    keyTuple.set(me + " " + frd);
                } else {
                    keyTuple.set(frd + " " + me);
                }
                fList.set(StringUtils.join(others, " "));
                context.write(keyTuple, fList);
            }
        }
	}
	public static class FofReducer extends Reducer<Text, Text, Text, Text> {
//		private void getTrio(int me, int friend, Set<String> fset, Context context) throws IOException, InterruptedException {
//			Iterator<String> itr = fset.iterator();
//			String other = "";
//			Text meText = new Text();
//			Text friendText = new Text();
//			int otherInt = 0;
//			while (itr.hasNext()) {
//				other = itr.next();
//				try {
//					otherInt = Integer.parseInt(other);
//				} catch (NumberFormatException e) {
//					e.printStackTrace();
//				}
//				if (otherInt > friend) {
//					meText.set(Integer.toString(me));
//					friendText.set(Integer.toString(friend) + " " + other);
//					System.out.println(me + " " + friend + " " + other);
//					context.write(meText, friendText);
//				}
//			}
//		}
		public void reduce(Text keyTuple, Iterator<Text> values,
				Context context) throws IOException {
//			String fString1;
//			String fString2;
//			String me;
//			String friend;
//			int meInt = 0;
//			int friendInt = 0;
			System.out.println("I am reducer\n");
//			try {
//				System.out.println("I am reducer\n");
//				String[] strs = StringUtils.split(keyTuple.toString(), " ");
//				me = strs[0];
//				friend = strs[1];
//				meInt = Integer.parseInt(me);
//				friendInt = Integer.parseInt(friend);
//				
//				fString1 = values.next().toString();
//				if (values.hasNext()) {
//					fString2 = values.next().toString();
//					Set<String> fSet = new HashSet<String>(Arrays.asList(fString1));
//					fSet.retainAll(new HashSet<String>(Arrays.asList(fString2)));
//					
//					getTrio(meInt, friendInt, fSet, context);
//					getTrio(friendInt, meInt, fSet, context);
//					
//				} else {
//					return;
//				}
//			} catch (NoSuchElementException e) {
//				e.printStackTrace();
//			} catch (Exception e) {
//				e.printStackTrace();
//			}
		}
	}
	public static void main(String[] args) throws Exception {
		Configuration conf = new Configuration();
	    String[] otherArgs = new GenericOptionsParser(conf, args).getRemainingArgs();
	    if (otherArgs.length != 2) {
	      System.err.println("Usage: fof <in> <out>");
	      System.exit(2);
	    }
	    Job job = new Job(conf, "fof");
	    job.setJarByClass(fof.class);
	    job.setMapperClass(FofMapper.class);
	    job.setCombinerClass(FofReducer.class);
	    job.setReducerClass(FofReducer.class);
	    job.setOutputKeyClass(Text.class);
	    job.setOutputValueClass(Text.class);
	    FileInputFormat.addInputPath(job, new Path(otherArgs[0]));
	    FileOutputFormat.setOutputPath(job, new Path(otherArgs[1]));
	    System.exit(job.waitForCompletion(true) ? 0 : 1);
	}
}
