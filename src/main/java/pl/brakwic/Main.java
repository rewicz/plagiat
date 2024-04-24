package pl.brakwic;

import com.fasterxml.jackson.databind.ObjectMapper;

import static pl.brakwic.CosineSimilarity.cosineSimilarity;
import static pl.brakwic.CosineSimilarity.createBowVector;
import static pl.brakwic.Printer.print;
import static pl.brakwic.UtilWord.prepareWords;

import java.io.InputStream;
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.util.*;
import java.util.concurrent.ExecutionException;
import java.util.stream.Collectors;

public class Main {

  static String bearerToken = "XXX";

  public static void main(String[] args) {

    Map<String,String> base = new HashMap<>();
    base.put("alg1", "[Reverse Bubble Sort]: This algorithm sorts a list in ascending order by repeatedly traversing it backward, swapping adjacent elements if they are in the wrong order, until no more swaps are needed, indicating the list is sorted.");
    base.put("alg2", "[Tree Node Update]: This algorithm searches through a tree structure for a node with a specified key, updates that node's children with new nodes, and sets its 'triggered' status to true if the node is found, applying the update recursively to all child nodes.");
    base.put("alg3", "[Find Parent Node]: This algorithm searches a tree structure to find the parent node of a specified node (identified by a matching key), returning the first parent node encountered in a depth-first search manner. If no such parent exists, it returns None.");
    base.put("alg4", "[Collect Keys Excluding Match]: This algorithm traverses a tree structure, collecting the keys of all nodes except those that match a specified key, and returns a list of these keys as strings, avoiding traversal beyond nodes that match the specified key.");
    base.put("alg5", "[Find Maximum Value]: This algorithm iterates through a list to identify and return the maximum value present. It raises an error if the list is empty.");
    base.put("alg6", "[Calculate Factorial]: This algorithm computes the factorial of a non-negative integer by multiplying all positive integers up to that number together, returning the result. It raises an error if the input number is negative.");
    base.put("alg7", "[Safe Element Retrieval]: This algorithm retrieves an element from a list at a specified index, returning a default value if the index is out of bounds or the list is None, ensuring safe access to list elements.");
    base.put("alg8", "[Bubble Sort]: This algorithm sorts a list by repeatedly traversing it, swapping adjacent elements if they are in the wrong order, and stops early if no swaps are made during a complete pass, indicating the list is sorted.");
    base.put("alg9", "[Sum of List]: This algorithm calculates and returns the total sum of all elements in a list.");
    base.put("alg10", "[Euclidean Algorithm for GCD]: This algorithm finds the greatest common divisor (GCD) of two numbers by repeatedly applying the Euclidean algorithm, where the second number is replaced by the remainder of the first number divided by the second number until the second number becomes zero.");
    base.put("alg11", "[Sum of List]: This algorithm computes and returns the sum of all elements within a list, effectively aggregating their total value.");
    base.put("alg12", "[Majority Element Finder]: This algorithm identifies the majority element in a list, which is an element that appears more than half of the time. It first uses the Boyer-Moore voting algorithm to find a candidate, then verifies if the candidate truly is the majority by counting its occurrences.");
    base.put("alg13", "[Sieve of Eratosthenes]: This algorithm generates a list indicating the primality of numbers up to n by initially assuming all numbers are prime and then iteratively marking the multiples of each prime number, starting from 2, as non-prime.");
    base.put("alg14", "[Insertion Sort]: This algorithm sorts a list by sequentially taking each element and inserting it into its correct position within the already sorted part of the list, ensuring each iteration leaves the list sorted up to the current element.");
    base.put("alg15", "[Shell Sort]: This algorithm enhances insertion sort by initially sorting elements far apart from each other using a gap, then gradually reducing the gap and sorting until the list is completely sorted.");
    base.put("alg16", "[Binary Conversion]: This algorithm converts a given number into its binary representation as a string, excluding the '0b' prefix that indicates binary in Python.");
    base.put("alg17", "[Dijkstra's Shortest Path Algorithm]: This algorithm calculates the shortest paths from a start node to all other nodes in a graph, initializing distances to infinity except for the start node, and iteratively updating the shortest distance to each node by considering all its unvisited neighbors and choosing the path that offers the lowest total distance.");
    base.put("alg18", "[Base Conversion]: This algorithm converts a given non-negative integer into a specified base, generating a list of digits in that base, and returns the list in the correct order, starting from the least significant digit to the most significant.");
    base.put("alg19", "[Insertion Sort]: This algorithm sorts a list by repeatedly taking each element and inserting it into its correct position within the sorted portion of the list, ensuring the list is sorted incrementally from the beginning to the end.");
    base.put("alg20", "[Shell Sort]: Enhances the insertion sort algorithm by initially sorting elements that are far apart from each other (determined by 'gap'), then gradually reducing the gap to perform finer sorting, until the gap is 1 and the list is fully sorted.");
    base.put("alg21", "[Binary Representation with Padding]: This algorithm converts a given number into a binary string representation, ensuring it is padded to 32 bits in length, filling with leading zeros if necessary.");
    base.put("alg22", "[Dijkstra's Algorithm for Shortest Paths]: This algorithm finds the shortest paths from a starting node to all other nodes in a weighted graph, updating the shortest known distance to each node iteratively and using a visited marker to avoid re-evaluating nodes.");
    base.put("alg23", "[Dihedral Group Permutation Check]: This algorithm checks if a sequence represented by a number conforms to a specific condition defined by dihedral group operations and a permutation table, evaluating the sequence in reverse and updating a condition variable through table lookups. It concludes by verifying if the final condition matches a target value, indicating conformity to the specified pattern.");
    base.put("alg24", "[Base Conversion with Count]: This algorithm converts a given non-negative integer into a specified base, then prepends the total count of digits in the converted form to the result, returning a list where the first element is the digit count followed by the digits of the number in the new base.");
    base.put("alg25", "[Reverse Base Conversion with Count]: This algorithm converts a list, where the first element indicates the count of the following elements (digits in a base), back into a decimal number by calculating the sum of each digit multiplied by its base raised to the corresponding power, effectively reversing a base conversion that includes a leading digit count.");
    base.put("alg26", "[Find Maximum Element]: This algorithm iterates through a collection to identify and return the maximum element. If the collection is empty, it returns a message indicating there is no input to process.");
    base.put("alg27", "[Find Nearest Unvisited Node]: This algorithm searches through a list of distances to find the unvisited node with the smallest distance, returning the index of that node. It is typically used in graph algorithms to select the next node to visit.");
    base.put("alg28", "[A Pathfinding Algorithm]**: This algorithm finds the shortest path between a start and end point in a graph using the A search algorithm. It calculates costs (g, h, f) for each node, where g is the cost from the start node, h is the heuristic estimated cost to the end node, and f is the total cost of the node. Nodes are added to an open list for exploration and moved to a closed list once explored, with the path being reconstructed from the end node to the start node once the end is reached.");
    base.put("alg29", "[Floyd-Warshall Algorithm]: This algorithm computes the shortest paths between all pairs of vertices in a graph, updating the distances matrix by considering each vertex as an intermediate point and minimizing the distance between every pair of vertices through it.");
    base.put("alg30", "[Boyer-Moore String Search Algorithm]: This algorithm efficiently searches for occurrences of a pattern within a string by using a preprocessed table to skip sections of the text that cannot possibly match the pattern, significantly reducing the number of comparisons. It updates its position within the string based on the last occurrence of the mismatched character in the pattern, moving more intelligently than simple character-by-character comparison.");
    base.put("alg31", "[Hash-Based Pattern Matching]: This algorithm uses hash values to search for a pattern within a string, comparing the hash of the pattern with the hash of current substrings of equal length. It increments a counter for each match found and moves through the string, recalculating hashes and checking against the pattern's hash. If no matches are found, it outputs a message indicating the absence of the pattern.");
    base.put("alg32", "[Caesar Cipher Shift]: This algorithm shifts each letter in a given string by a specified number of positions in the alphabet, wrapping around if necessary, and leaves non-alphabet characters unchanged, effectively implementing a Caesar cipher encryption or decryption.");
    base.put("alg33", "[Bubble Sort]: This algorithm sorts a list by repeatedly comparing and swapping adjacent elements if they are in the wrong order, ensuring each element moves to its correct position through a series of passes over the entire list.");
    base.put("alg34", "Implements quick sort to sort a list of elements.");
    base.put("alg35", "Finds the minimum spanning tree of a graph using the Prim's algorithm.");


    InputStream inputStream = Main.class.getClassLoader().getResourceAsStream("test.txt");

    if (inputStream == null) {
      System.out.println("Nie można znaleźć pliku test.txt");
      return;
    }

    StringBuilder contentBuilder = new StringBuilder();
    try (Scanner scanner = new Scanner(inputStream)) {
      while (scanner.hasNextLine()) {
        String line = scanner.nextLine();
        contentBuilder.append(line).append("\n");
      }
    }

    ObjectMapper mapper = new ObjectMapper();
    String requestBody;
    try {
      requestBody = mapper.writeValueAsString(new JsonModel("gpt-3.5-turbo", "Write this in Python, and let the response contain only the Python code.\n\n" + contentBuilder.toString(), 50));
    } catch (Exception e) {
      System.err.println("Error creating JSON: " + e.getMessage());
      return;
    }

    HttpClient client = HttpClient.newHttpClient();
    HttpRequest request = HttpRequest.newBuilder()
            .uri(URI.create("https://api.openai.com/v1/chat/completions"))
            .header("Authorization", "Bearer " + bearerToken)
            .header("Content-Type", "application/json")
            .POST(HttpRequest.BodyPublishers.ofString(requestBody))
            .build();

    String pythonString = "";
    try {
      pythonString = client.sendAsync(request, HttpResponse.BodyHandlers.ofString())
              .thenApply(HttpResponse::body)
              .get();
      System.out.println(pythonString);

    } catch (InterruptedException | ExecutionException e) {
      System.err.println("Error during API request: " + e.getMessage());
      Thread.currentThread().interrupt();
    }

    String requestBody2 = "";
    try {
      requestBody2 = mapper.writeValueAsString(new JsonModel("gpt-3.5-turbo", "Describe each algorithm separately in 1-2 sentences without using variable names, focus on the logic of the algorithm, name every algorithm in brackets square brackets ,dont use def name of algorithm\n\n" + pythonString,( 50)));
    } catch (Exception e) {
      System.err.println("Error creating JSON: " + e.getMessage());
    }
    HttpRequest request2 = HttpRequest.newBuilder()
            .uri(URI.create("https://api.openai.com/v1/chat/completions"))
            .header("Authorization", "Bearer " + bearerToken)
            .header("Content-Type", "application/json")
            .POST(HttpRequest.BodyPublishers.ofString(requestBody2))
            .build();

    String description = "";
    try {
      description = client.sendAsync(request2, HttpResponse.BodyHandlers.ofString())
              .thenApply(HttpResponse::body)
              .get();
      System.out.println(description);
    } catch (InterruptedException | ExecutionException e) {
      System.err.println("Error during API request: " + e.getMessage());
      Thread.currentThread().interrupt();
    }



    List<String> search1 = prepareWords(description);
    Map<String, Integer> searchVector = createBowVector(search1);

    Map<String, Double> resultMap = new HashMap<>();

    for (String key : base.keySet()) {
      List<String> words2 = prepareWords(base.get(key));
      Map<String, Integer> vector2 = createBowVector(words2);
      resultMap.put(key, cosineSimilarity(searchVector, vector2));
    }

      Map<String, Double> filteredMap = resultMap.entrySet().stream()
              .filter(entry -> entry.getValue() > 0.5)
              .collect(Collectors.toMap(Map.Entry::getKey, Map.Entry::getValue));

    print(filteredMap);
  }

  static class JsonModel {
    public String model;
    public String prompt;
    public int max_tokens;

    public JsonModel(String model, String prompt, int max_tokens) {
      this.model = model;
      this.prompt = prompt;
      this.max_tokens = max_tokens;
    }
  }

}

