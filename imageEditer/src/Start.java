import java.io.*;
import java.util.ArrayList;
import java.util.List;

public class Start {

    public void start()  {
        try {
            ProcessBuilder builder = new ProcessBuilder(
                    "cmd.exe", "/c", "cd \"C:\\Users\\CMA\\Desktop\\ScrapyPicture\\ScrapyPicture\" && python start.py");
            builder.redirectErrorStream(true);
            Process p = builder.start();
            BufferedReader r = new BufferedReader(new InputStreamReader(p.getInputStream()));
            String line;
            while (true) {
                line = r.readLine();
                if (line == null) { break; }
                System.out.println(line);
            }
        } catch (IOException e){
            e.printStackTrace();
        }
    }

    public void setUrl(String URL){
        try {
            FileInputStream fileInputStream = new FileInputStream("C:\\Users\\CMA\\Desktop\\ScrapyPicture\\ScrapyPicture\\spiders\\PicSpider.py");
            InputStreamReader inputStreamReader = new InputStreamReader(fileInputStream,"utf-8");
            BufferedReader bufferedReader = new BufferedReader(inputStreamReader);
            String str = "";
            List<String> code = new ArrayList<>();
            while((str=bufferedReader.readLine())!=null){
                code.add(str);
            }
            code.set( 8,"    url = \""+URL+"\"");

            File file = new File("C:\\Users\\CMA\\Desktop\\ScrapyPicture\\ScrapyPicture\\spiders\\PicSpider.py");
            FileOutputStream fileOutputStream = new FileOutputStream(file);
            OutputStreamWriter outputStreamWriter = new OutputStreamWriter(fileOutputStream);
            BufferedWriter bufferedWriter = new BufferedWriter(outputStreamWriter);
            for (String s : code){
                bufferedWriter.write(s);
                bufferedWriter.newLine();
            }
            bufferedWriter.flush();
        }catch (Exception e){
            e.printStackTrace();
        }

    }

    public static void main(String[] args) throws IOException {
//        Start start = new Start();
//        String url = "https://item.jd.com/502250.html";
//        //需要爬取的京东商品地址
//        start.setUrl(url);
//        start.start();

        Editer editer = new Editer();

        String src = "C:\\Users\\CMA\\Desktop\\tb\\";
        String name = "罗技MK270";
        String format = ".png";
        //商品介绍的截图位置
        editer.crop(src, name, format, true);
    }
}
