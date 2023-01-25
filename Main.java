import java.util.Scanner;
class Main {
    
    public static int Balok(int panjang,int lebar,int tinggi){
        int hasilB = panjang * lebar * tinggi;
        return hasilB;
    }
    
    public static void main(String[] args) {
        System.out.println("Balok Volume Kalkulator Java");
        System.out.println("====================");
        System.out.println("By Andhika Eka Santosa");
        System.out.println("====================");
        
        Scanner inputPanjang = new Scanner(System.in);
        System.out.println("Masukkan Panjang");
        int panjangg = inputPanjang.nextInt();
            
        Scanner inputLebar = new Scanner(System.in);
        System.out.println("Masukkan Panjang");
        int lebarr = inputLebar.nextInt();

        Scanner inputTinggi = new Scanner(System.in);
        System.out.println("Masukkan Panjang");
        int tinggi = inputPanjang.nextInt();  
            
        System.out.println("Jawabannya Adalah " + Balok(panjangg,lebarr,tinggi) + "cm kubik"); 
    }
}
