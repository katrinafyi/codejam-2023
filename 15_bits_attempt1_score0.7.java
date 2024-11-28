import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.function.*;
import java.util.regex.*;
import java.util.stream.*;
import static java.util.stream.Collectors.joining;
import static java.util.stream.Collectors.toList;

class Result {

    /*
     * Complete the 'bits' function below.
     *
     * The function is expected to return a LONG_INTEGER_ARRAY.
     * The function accepts LONG_INTEGER_ARRAY a as parameter.
     */

    public static List<Integer> bits(List<Integer> a) {
    // Write your code here
        List<Integer> out = new ArrayList<>();
        for (int x : a) {
            //int right = x & -x;
            out.add(x & (x-1));
        }
        return out;

    }

}

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        int nn = (int)Long.parseLong(bufferedReader.readLine().trim());

        List<Integer> aa = IntStream.range(0, nn).mapToObj(i -> {
            try {
                return bufferedReader.readLine().replaceAll("\\s+$", "");
            } catch (IOException ex) {
                throw new RuntimeException(ex);
            }
        })
            .map(String::trim)
            .map(Integer::parseInt)
            .collect(toList());

        List<Integer> yy = Result.bits(aa);

        bufferedWriter.write(
            yy.stream()
                .map(Object::toString)
                .collect(joining("\n"))
            + "\n"
        );

        bufferedReader.close();
        bufferedWriter.close();
    }
}
