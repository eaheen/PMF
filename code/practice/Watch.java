import java.time.*;
import java.util.*;
public class Watch{
    LocalTime timeNow;
    Instant rightNow;
    double startTime;
    double endTime;
    public double getStart(){
        return this.startTime;
    }
    public double getEnd(){
        return this.endTime;
    }
    public String getTimeNow(){
        return String.format("%02d:%02d:%02d",timeNow.getHour(),timeNow.getMinute(),timeNow.getSecond());
    }
    public void start(){
        this.startTime = (double)rightNow.toEpochMilli();
    }
    public void stop(){
        this.endTime = (double)rightNow.now();
    }
    public double elapsed(){
        return(this.endTime - this.startTime);
    }
    public Watch(){
        this.startTime = startTime;
        this.endTime = endTime;
    }
    public static List<Integer> generateRandomArray(int n){
        ArrayList<Integer> list = new ArrayList<Integer>(n);
        Random random = new Random();
        for (int i = 0; i < n; i++)
        {
            list.add(random.nextInt(1000));
        }
       return list;
    }  
    public static void main(String[] args){
        Watch w = new Watch();
        List<Integer> shortList = generateRandomArray(25000);
        List<Integer> longList = generateRandomArray(50000);
        w.start();
        Collections.sort(shortList);
        w.stop();
        System.out.println("Long List: "+w.elapsed());
        w.start();
        Collections.sort(longList);
        w.stop();
        System.out.println("Short List: "+w.elapsed());
    }
}