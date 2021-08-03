package com.utec.kusastore.model;

public class Product {
    private int id;
    private String nombre;
    private double precio;
    private String descripcion;
    private String img_url;
    private int stock;

    public Product(int id, String nombre, double precio, String descripcion, String img_url, int stock) {
        this.id = id;
        this.nombre = nombre;
        this.precio = precio;
        this.descripcion = descripcion;
        this.img_url = img_url;
        this.stock = stock;
    }
}
