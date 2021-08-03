package com.utec.kusastore;

import androidx.appcompat.app.AppCompatActivity;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import android.app.Activity;
import android.os.Bundle;

import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.JsonArrayRequest;
import com.android.volley.toolbox.Volley;

import org.json.JSONArray;

public class MainActivity extends AppCompatActivity {
    RecyclerView mRecyclerView;
    RecyclerView.Adapter mAdapter;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        String username = getIntent().getExtras().getString("username");
        setTitle("Kusa Store");
    }

    @Override
    protected void onResume() {
        super.onResume();
        mRecyclerView.setLayoutManager(new LinearLayoutManager(this));
        getProducts();
    }
    public Activity getActivity(){
        return this;
    }

    public void getProducts(){
        String uri = "http://10.0.2.2:8000/users";
        RequestQueue queue = Volley.newRequestQueue(this);
        JSONArray jsonMessage = new JSONArray();

        JsonArrayRequest request = new JsonArrayRequest(
                Request.Method.GET,
                uri,
                jsonMessage, // empty message
                new Response.Listener<JSONArray>() {
                    @Override
                    public void onResponse(JSONArray response) {
                        //Step1. Create element view for each user.
                        //Step2. Create dynamically elements view and inject to Recyc View
                        mAdapter = new ChatAdapter(response, getActivity(), user_id);
                        mRecyclerView.setAdapter(mAdapter);
                    }
                },
                new Response.ErrorListener() {
                    @Override
                    public void onErrorResponse(VolleyError error) {
                        //TODO process the error
                        error.printStackTrace();
                    }
                }
        );

        //RequestQueue queue = Volley.newRequestQueue(this);
        queue.add(request);


    }


}