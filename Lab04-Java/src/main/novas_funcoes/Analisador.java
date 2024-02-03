package novas_funcoes;

import java.util.ArrayList;
import java.util.stream.IntStream;

public class Analisador {
    int melhor = -1;
    double melhor_valor = 0;

    public int[] acha_sequencia(int[] valores, double[] probs){
        int tamanho = valores.length;
        ArrayList<Integer> ordem = new ArrayList<Integer>();
        ArrayList<Integer> usados = new ArrayList<Integer>();
        while (ordem.size() < tamanho){ 
            int x = seleciona(probs, valores, usados);
            ordem.add(x);
            usados.add(x); 
        }
        int[] resultado = new int[ordem.size()];
        for (int i = 0; i < ordem.size(); i++){
            resultado[i] = ordem.get(i);
        }
        return resultado;
    }

    public int seleciona(double[] probs, int[] valores, ArrayList<Integer> usados){
        melhor = -1;
        melhor_valor = 0;
        // Criar um fluxo de inteiros de 0 a 9 (exclusivo)
        IntStream.range(0, probs.length).forEach(n -> {
            if (!usados.contains(n)){
                double valor = valores[n] * probs[n] * probs[n];
                if (valor > melhor_valor){
                    melhor = n;
                    melhor_valor = valor;
                }
            }
        });
        return melhor;
    }
       
}
