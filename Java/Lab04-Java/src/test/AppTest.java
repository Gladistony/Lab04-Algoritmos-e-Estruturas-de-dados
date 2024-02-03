package test;

import static org.junit.jupiter.api.Assertions.assertTrue;

import java.util.Arrays;

import org.junit.Test;
import novas_funcoes.Analisador;

public class AppTest {

    @Test
    public void test_vazio() {
        Analisador a = new Analisador();
        double[] prob1 = {0.8};
        int[] freq1 = {10};
        double[] prob2 = {0.8, 0.4};
        int[] freq2 = {10, 5};
        double[] prob3 = {0.5, 0.9, 0.2, 0.6};
        int[] freq3 = {3, 1, 4, 1};

        int [] array1 = {0};
        int [] array1_1 = a.acha_sequencia(freq1, prob1);
        assertTrue(Arrays.equals(array1, array1_1));

        int [] array2 = {0,1};
        int [] array2_1 = a.acha_sequencia(freq2, prob2);
        assertTrue(Arrays.equals(array2, array2_1));

        int [] array3 = {1, 0, 3, 2};
        int [] array3_1 = a.acha_sequencia(freq3, prob3);
        assertTrue(Arrays.equals(array3, array3_1));
    }

}
