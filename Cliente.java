package Academia;

import java.time.LocalDateTime;

public class Cliente {
    
    private String nome;
    private LocalDateTime data_de_cadastro;
    private String data_de_nascimento;
    private String plano;
    private String endereco;
    private String cpf;
    private String nivel;

    public Cliente(String nome, String data_de_nascimento, String plano, String endereco, String cpf, String nivel){
        this.nome = nome;
        this.data_de_cadastro = LocalDateTime.now();
        this.data_de_nascimento = data_de_nascimento;
        this.plano = plano;
        this.endereco = endereco;
        this.cpf = cpf;
        this.nivel = nivel;
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public LocalDateTime getData_de_cadastro() {
        return data_de_cadastro;
    }

    public String getData_de_nascimento() {
        return data_de_nascimento;
    }

    public String getPlano() {
        return plano;
    }

    public void setPlano(String plano) {
        this.plano = plano;
    }

    public String getEndereco() {
        return endereco;
    }

    public void setEndereco(String endereco) {
        this.endereco = endereco;
    }

    public String getCpf() {
        return cpf;
    }

    public String getNivel() {
        return nivel;
    }

    public void setNivel(String nivel) {
        this.nivel = nivel;
    }

    @Override
    public String toString(){
        return "Nome: " + getNome() + "\nCPF: " + getCpf() + "\nEndereço: " 
        + getEndereco() + "\nData de nascimento: " + getData_de_nascimento() + 
        "\nData de cadastro: " + getData_de_cadastro() + "\nPlano: " + getPlano() + "\nNível: " + getNivel();
    }
}