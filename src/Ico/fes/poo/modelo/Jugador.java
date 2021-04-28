/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Ico.fes.poo.modelo;

/**
 *
 * @author mez29
 */
public class Jugador {
    private String nombre;
    private String apellidoPaterno;
    private String apellidoMaterno;
    private String apodo;
    private String equipo;
    private String pais;
    private String posicion;
    private int numero; 

    public Jugador () {
        
    }
    
    public Jugador (String nombre, String apellidoPaterno, String apellidoMaterno, String apodo, String equipo, String pais, String posicion, int numero) {
        this.nombre = nombre;
        this.apellidoPaterno = apellidoPaterno;
        this.apellidoMaterno = apellidoMaterno;
        this.apodo = apodo;
        this.equipo = equipo;
        this.pais = pais;
        this.posicion = posicion;
        this.numero = numero;  
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public String getApellidoPaterno() {
        return apellidoPaterno;
    }

    public void setApellidoPaterno(String apellidoPaterno) {
        this.apellidoPaterno = apellidoPaterno;
    }

    public String getApellidoMaterno() {
        return apellidoMaterno;
    }

    public void setApellidoMaterno(String apellidoMaterno) {
        this.apellidoMaterno = apellidoMaterno;
    }

    public String getApodo() {
        return apodo;
    }

    public void setApodo(String apodo) {
        this.apodo = apodo;
    }

    public String getEquipo() {
        return equipo;
    }

    public void setEquipo(String equipo) {
        this.equipo = equipo;
    }

    public String getPais() {
        return pais;
    }

    public void setPais(String pais) {
        this.pais = pais;
    }

    public String getPosicion() {
        return posicion;
    }

    public void setPosicion(String posicion) {
        this.posicion = posicion;
    }

    public int getNumero() {
        return numero;
    }

    public void setNumero(int numero) {
        this.numero = numero;
    }

    @Override
    public String toString() {
        return "Jugador{" + "Nombre=" + nombre + ", apellidoPaterno=" 
                + apellidoPaterno + ", apellidoMaterno=" + apellidoMaterno 
                +", Apodo="+ apodo + ", equipo=" + equipo + ", pais=" + pais
                + ", posicion=" + posicion + ", numero=" + numero + '}';
    }

}