package com.utec.kusastore;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.EditText;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;

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

public class LoginActivity extends AppCompatActivity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_login);
    }

    public void showMessage(String message) {
        Toast.makeText(this, message, Toast.LENGTH_LONG).show();
    }

    public void onLoginClicked(View view){
        EditText txtUsername = (EditText) findViewById(R.id.txt_username_input);
        EditText txtPassword = (EditText) findViewById(R.id.txt_password_input);
        String username = txtUsername.getText().toString();
        String password = txtPassword.getText().toString();

        Map<String, String> message = new HashMap<>();
        message.put("username", username);
        message.put("password", password);

        JSONObject jsonMessage = new JSONObject(message);

        JsonObjectRequest request = new JsonObjectRequest(
                Request.Method.POST,
                "http://10.0.2.2:8000/login",
                jsonMessage,
                new Response.Listener<JSONObject>() {
                    @Override
                    public void onResponse(JSONObject response) {
                        showMessage("Ingreso satisfactorio");
                        try {
                            String username = response.getString("username");
                            int role = response.getInt("role");
                            int userId = response.getInt("userid");
                            goToDashboard(username, role, userId);
                        } catch (JSONException e) {
                            e.printStackTrace();
                        }
                    }
                },
                new Response.ErrorListener() {
                    @Override
                    public void onErrorResponse(VolleyError error) {
                        showMessage("Usted no está registrado");
                    }
                }
        );
        RequestQueue queue = Volley.newRequestQueue(this);
        queue.add(request);
    }

    private void goToDashboard(String username, int role, int userId){
        Intent intent;
        if(role == 1){
            intent = new Intent(this, AdminActivity.class);
        }else {
            intent = new Intent(this, UserActivity.class);
        }
        intent.putExtra("username", username);
        intent.putExtra("userId", userId);
        intent.putExtra("role", role);
    }
}