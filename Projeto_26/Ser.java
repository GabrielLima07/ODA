import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;

public class Ser {
    
    public static void main(String [] args) {
        serializar();
        desserializar();
    }

    public static void serializar() {
        Vendedor v1 = new Vendedor("João Silva", 22, 2715.35);
        FileOutputStream x = null;
        ObjectOutputStream y = null;
        
        try {
        // esse arquivo será criado no mesmo diretório do programa, com o nome "exemplo"
        x = new FileOutputStream("exemplo.txt"); 
        y = new ObjectOutputStream(x);
        // serialização do objeto v1
        y.writeObject(v1); 

        // possíveis cenários que podem ocorrer ao tentar serializar o objeto
        } catch (FileNotFoundException e) { 
            System.out.println("O arquivo não foi encontrado");
        } catch (IOException e) {
            System.out.println("Erro ao tentar criar o arquivo");

        // fechar o arquivo, caso tenha sido serializado com sucesso
        } finally {
            if (y != null) {
                try {
                    y.close();
                } catch (IOException e) {
                    System.out.println("Erro ao tentar fechar o arquivo");
                }
            }
        }
    }

    public static void desserializar() {
        Vendedor v1 = null;
        FileInputStream x = null;
        ObjectInputStream y = null;

        try {
            x = new FileInputStream("exemplo.txt");
            y = new ObjectInputStream(x);

            // conversão do objeto que está sendo desserializado para classe Vendedor
            v1 = (Vendedor)y.readObject();

            // exibição dos dados do objeto
            System.out.printf("Nome: %s\nIdade: %d\nSalário: R$%.2f\nNúmero de vendas: %d",
            v1.getNome(), v1.getIdade(), v1.getSalario(), v1.getNumeroVendas());

        // possívies cenários que podem ocorrer ao tentar desserializar o objeto
        } catch (ClassNotFoundException e) { 
            System.out.println("A classe não foi encontrada");
        } catch (IOException e) {
            System.out.println("Erro ao tentar criar o arquivo");

        // se o objeto y(desserealizador) for diferente de nulo, então o arquivo será fechado
        } finally {
            if (y != null) {
                try {
                    y.close();
                } catch (IOException e) {
                    System.out.println("Erro ao tentar fechar o arquivo");
                }
            }
        }
    }
}
