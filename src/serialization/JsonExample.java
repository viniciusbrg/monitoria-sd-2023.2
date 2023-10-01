package serialization;

import com.google.gson.Gson;

public class JsonExample {
    public static void main(String[] args) {
        var pessoa = new Pessoa("Chiquinho", "Fortaleza", 1, 1);

        var gson = new Gson();

        var json = gson.toJson(pessoa);
        System.out.println(json);

        var pessoaOriginal = gson.fromJson(json, Pessoa.class);

        System.out.println(pessoaOriginal);
    }
}
