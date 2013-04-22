import java.io.IOException;

import org.apache.commons.lang.StringUtils;
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Reducer;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
import org.apache.hadoop.util.GenericOptionsParser;



public class fof {
	public static class FofMapper 
            extends Mapper<Object, Text, Text, IntWritable> {

        private Text trio = new Text();
        private final static IntWritable one = new IntWritable(1);

		public void map(Object key, Text values, Context context) throws IOException, InterruptedException {
			String line = values.toString();
			String[] ppls = line.split(" ");
            String me; 
            String frd;

            me = ppls[0];
            for (int i = 1; i < ppls.length; i++) {
                frd = ppls[i];
                for (int j = 1; j < ppls.length; j++) {
                	if (j != i) {
	                    trio.set(me + " " + frd + " " + ppls[j]);
	                    context.write(trio, one);
	                    trio.set(frd + " " + me + " " + ppls[j]);
	                    context.write(trio, one);
                	}
                }
            }
        }
	}
	public static class FofReducer 
            extends Reducer<Text, IntWritable, Text, IntWritable> {

		public void reduce(Text trio, Iterable<IntWritable> values,
				Context context) throws IOException, InterruptedException {
            int sum = 0;
            for (IntWritable val : values) {
                sum += val.get();
            }
            if (sum > 1) {
                String[] ppls = StringUtils.split(trio.toString(), " ");
                int frnd = Integer.parseInt(ppls[1]);
                int other = Integer.parseInt(ppls[2]);
                if (frnd < other) {
                    context.write(trio, null);
                }
            }
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
	    job.setReducerClass(FofReducer.class);
	    job.setOutputKeyClass(Text.class);
	    job.setOutputValueClass(IntWritable.class);
	    FileInputFormat.addInputPath(job, new Path(otherArgs[0]));
	    FileOutputFormat.setOutputPath(job, new Path(otherArgs[1]));
	    System.exit(job.waitForCompletion(true) ? 0 : 1);
	}
}
