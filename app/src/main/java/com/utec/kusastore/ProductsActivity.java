package com.utec.kusastore;

import android.os.Bundle;

import androidx.appcompat.app.AppCompatActivity;

import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.toolbox.JsonArrayRequest;
import com.android.volley.toolbox.Volley;
import com.utec.kusastore.model.Product;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import java.util.List;

public class ProductsActivity extends AppCompatActivity {

    private List<Product> products;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_products);
    }

    public void getProducts(){
        String uri = "http://10.0.2.2:8000/products";
        RequestQueue queue = Volley.newRequestQueue(this);
        JSONArray jsonMessage = new JSONArray();


    }


}
/*
                new Response.Listener<JSONArray>() {
                    @Override
                    public void onResponse(JSONArray response) {
                        for(int i = 0; i < response.length(); ++i){
                            try {
                                JSONObject jsonObject = response.getJSONObject(i);
                                int id = jsonObject.getInt("id");
                                String nombre = jsonObject.getString("nombre");
                                double precio = jsonObject.getInt("precio");
                                String descripcion = jsonObject.getString("descripcion");
                                String img_url = jsonObject.getString("img_url");
                                int stock = jsonObject.getInt("stock");

                            }catch (JSONException e){
                                e.printStackTrace();
                            }
                        }
                    }
                }
 */