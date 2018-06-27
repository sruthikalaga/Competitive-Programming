public class Temperature_Tracker {
    
    static int freq[] = new int[111]; 
    static int Freq = 0;
    static int mode;  
    static int count = 0;
    static double total = 0.0;
    static double mean;
    static int min;
    static int max;

    public static void insert(int temp) {

        freq[temp]++;
        if (freq[temp] > Freq) {
            mode = temp;
            Freq = freq[temp];
        }

        count++;
        total += temp;
        mean = total / count;
        if (max == null || temp > max) {
            max = temp;
        }
        if (min == null || temp < min) {
            min = temp;
        }
    }


    public static Double Mean() {

        return mean;

    }


    public static Integer Mode() {

        return mode;

    }

    public static Integer Max() {

        return max;

    }


    public static Integer Min() {

        return min;

    }
}
