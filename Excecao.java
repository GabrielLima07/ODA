// Projeto 27
import java.util.Scanner;


public class Excecao {

    public static void main(String [] args) {

        int n1, n2;
        int divisao;
        Scanner input = new Scanner(System.in);
        
        System.out.println("-DIVISÃO DE NÚMEROS INTEIROS-");
        System.out.println("Insira um número inteiro");
        n1 = input.nextInt();
        System.out.println("Insira mais um número inteiro");
        n2 = input.nextInt();
        input.close();

        try {
            divisao = n1 / n2;
            System.out.println(n1 + "/" + n2 + " = " + divisao);
        } catch (ArithmeticException e) {
            System.out.println("Não é possível dividir um número por 0");
        }

        System.out.println("Fim do programa");
    }
}