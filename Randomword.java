
import edu.princeton.cs.algs4.StdIn;
import edu.princeton.cs.algs4.StdOut;
import edu.princeton.cs.algs4.StdRandom;

class Randomword {
public static void main(String[] args) {
      int index = 0;
      String champion = " ";

      String words=StdIn.readLine();
      String[] word=words.split(" ");

      while(index<word.length){
        boolean accept = StdRandom.bernoulli(1 / (index + 1.0));
        if (accept) {
           champion = word[index];
    
        index++;
    }}
    StdOut.println(champion);
  }
}