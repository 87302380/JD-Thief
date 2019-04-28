import javax.imageio.ImageIO;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;

public class Editer {

    public BufferedImage getImage (String URL) {
        File file = new File(URL);
        BufferedImage image = null ;
        try {
            image = ImageIO.read(file);
        } catch(IOException e){
            System.out.println("no find file");
            e.printStackTrace();
        }
        return image;
    }

    public void save (BufferedImage image, String URL, String format){
        try {
            ImageIO.write(image, format, new File(URL));
        }catch (IOException e){
            e.printStackTrace();
        }
    }
    public void save (BufferedImage image, String URL){
        this.save(image, URL, "png");
    }

    public BufferedImage format(BufferedImage image){
        return image.getSubimage(123,0, 742, image.getHeight());
    }

    public void crop(String src, String name, String format, boolean isFormat){
        String URL = src + name + format;
        BufferedImage image = null;

        if (!isFormat){
            image = this.format(this.getImage(URL));
        }else {
            image = this.getImage(URL);
        }

        int width = image.getWidth();
        int height = image.getHeight();
        int part = height/2400;

        if (part==0){
            BufferedImage imagePart = image.getSubimage(0,0, width, height%2400);
            String fileName = src + name + "-" + String.valueOf(part)+ format;
            this.save(imagePart,fileName);
        }else {
            for (int i = 0; i<part;i++){
                BufferedImage imagePart = image.getSubimage(0,2400*(i), width,2400);
                String fileName = src + name + "-" + String.valueOf(i)+ format;
                this.save(imagePart,fileName);
            }
            BufferedImage imagePart = image.getSubimage(0,2400*(part), width, height%2400);
            String fileName = src + name + "-" + String.valueOf(part)+ format;
            this.save(imagePart,fileName);
        }
    }

    public static void main(String[] args) throws IOException {
        Editer editer = new Editer();

        String src = "C:\\Users\\CMA\\Desktop\\tb\\";
        String name = "MK120";
        String format = ".png";

        editer.crop(src, name, format, true);
    }

}