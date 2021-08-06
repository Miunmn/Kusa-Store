package com.utec.kusastore;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;
import androidx.recyclerview.widget.RecyclerView;

import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.JsonObjectRequest;
import com.android.volley.toolbox.Volley;

import org.json.JSONException;
import org.json.JSONObject;

import java.util.HashMap;
import java.util.Map;

public class CreateActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_create);
    }

    public void showMessage(String message) {
        Toast.makeText(this, message, Toast.LENGTH_LONG).show();
    }
    public void onCreateProductClicked(View view){
        EditText txt_productname = (EditText) findViewById(R.id.txt_productname);
        EditText txt_productdescrip = (EditText) findViewById(R.id.txt_productdescrip);
        EditText txt_productprice = (EditText) findViewById(R.id.txt_productprice);
        EditText txt_productstock = (EditText) findViewById(R.id.txt_productstock);
        EditText txt_productoimageurl = (EditText) findViewById(R.id.txt_productoimageurl);
        String nombre = txt_productname.getText().toString();
        String descripcion = txt_productdescrip.getText().toString();
        String precio = txt_productprice.getText().toString();
        String stock = txt_productstock.getText().toString();
        String imagen = txt_productoimageurl.getText().toString();
        Map<String, String> payload = new HashMap<>();
        payload.put("nombre", nombre);
        payload.put("descripcion", descripcion);
        payload.put("precio", precio);
        payload.put("stock", stock);
        payload.put("imagen", imagen);
        JSONObject jsonMessage = new JSONObject(payload);
        JsonObjectRequest request = new JsonObjectRequest(
                Request.Method.POST,
                "http://10.0.2.2:8080/createproductmobile",
                jsonMessage,
                new Response.Listener<JSONObject>() {
                    @Override
                    public void onResponse(JSONObject response) {
                        try {
                            showMessage(response.getString("message"));
                            if(response.getString("message").equals("Producto creado con éxito")){
                                showMessage("Producto creado!");
                            }
                        } catch (JSONException e) {
                            // TODO Auto-generated catch block
                            e.printStackTrace();
                        }
                    }
                },
                new Response.ErrorListener() {
                    @Override
                    public void onErrorResponse(VolleyError error) {
                        showMessage(error.toString());
                        showMessage("Error al crear producto");
                    }
                }
        );
        RequestQueue queue = Volley.newRequestQueue(this);
        queue.add(request);
    }

}
