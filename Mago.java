//Projeto 22
// Classe
public class Mago {

    // Atributos (variáveis)
    String habilidadePrincipal;
    int pontosExperiencia;
    int nivel;

    // Método e incremento
    void lerLivro() {
        pontosExperiencia += 50;
    }
}


// Objeto 1
class MagoNovato {
    
    public static void main(String [] args) {

        Mago m1 = new Mago();
        Mago m2 = new Mago();

        m1.habilidadePrincipal = "Feixe de luz";
        m1.pontosExperiencia = 100;
        m1.nivel = 1;

        m2.habilidadePrincipal = "Feixe de luz";
        m2.pontosExperiencia = 200;
        m2.nivel = 2;

        m1.lerLivro();
        m2.lerLivro();

        System.out.println("Experiência atual(Mago 1): " + m1.pontosExperiencia);
        System.out.println("Experiência atual(Mago 2): " + m2.pontosExperiencia);
    }
}


// Objeto 2
class MagoAprendiz {

    public static void main(String [] args) {

        Mago m1 = new Mago();

        m1.habilidadePrincipal = "Tempestade de raios";
        m1.pontosExperiencia = 1000;
        m1.nivel = 10;

        m1.lerLivro();

        System.out.println("Experiência atual: " + m1.pontosExperiencia);
    }    
}


// Objeto 3
class MagoSupremo {

    public static void main(String [] args) {

        Mago m1 = new Mago();

        m1.habilidadePrincipal = "Bola de fogo";
        m1.pontosExperiencia = 9900;
        m1.nivel = 99;

        m1.lerLivro();

        System.out.println("Experiência atual: " + m1.pontosExperiencia);
    }    
}
