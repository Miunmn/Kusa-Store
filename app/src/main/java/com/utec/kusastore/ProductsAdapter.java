package com.utec.kusastore;

import android.annotation.SuppressLint;
import android.content.Context;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.RelativeLayout;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.GridLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import com.squareup.picasso.Picasso;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import java.io.File;

public class ProductsAdapter extends  RecyclerView.Adapter<ProductsAdapter.ViewHolder>  {
    public JSONArray products;
    private Context context;
    public ProductsAdapter(JSONArray products, Context context){
        this.products = products;
        this.context = context;
    }

    @NonNull
    @Override
    public ViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        View view = LayoutInflater.from(parent.getContext()).inflate(R.layout.element_view, parent, false);
        return new ViewHolder(view);
    }


    @SuppressLint("SetTextI18n")
    @Override
    public void onBindViewHolder(@NonNull ViewHolder holder, int position) {
        try {
            final JSONObject product = products.getJSONObject(position);

            String name = product.getString("nombre");
            Double precio = product.getDouble("precio");
            String image = product.getString("img_url");
            String sprecio = String.valueOf(precio);

            holder.p_name.setText(name);
            holder.p_price.setText("Precio: "+sprecio);
            Picasso.get().load(image).into(holder.p_image);

            holder.p_button.setTag(R.id.tag_first, name);

        } catch (JSONException e) {
            e.printStackTrace();
        }
    }
    @Override
    public int getItemCount() {
        return products.length();
    }

    public class ViewHolder extends RecyclerView.ViewHolder{
        ImageView p_image;
        TextView p_name;
        TextView p_price;
        Button p_button;

        RelativeLayout container;
        public ViewHolder(View itemView){
            super(itemView);
            p_name = itemView.findViewById(R.id.element_view_name);
            p_price = itemView.findViewById(R.id.element_view_price);
            p_image = itemView.findViewById(R.id.element_view_image);
            p_button = itemView.findViewById(R.id.element_view_buybutton);
            container = itemView.findViewById(R.id.element_view_container);
            GridLayoutManager layoutManager = new GridLayoutManager(context, 2);
        }
    }

}
