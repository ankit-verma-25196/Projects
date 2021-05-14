package in.thekites.quizlite;

import android.content.DialogInterface;
import android.content.Intent;
import android.support.v7.app.AlertDialog;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.ImageButton;

public class RulesActivity extends AppCompatActivity {

    ImageButton back,home,close;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_rules);

        back=(ImageButton)findViewById(R.id.button_back);
        home=(ImageButton)findViewById(R.id.button_home);
        close=(ImageButton)findViewById(R.id.button_close);



        back.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {

                                Intent i=new Intent(RulesActivity.this,MainActivity.class);
                                startActivity(i);
                                finish();
                            }

        });



        home.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {

                Intent i=new Intent(RulesActivity.this,MainActivity.class);
                startActivity(i);
                finish();
            }

        });
        close.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {

                Intent i=new Intent(RulesActivity.this,MainActivity.class);
                startActivity(i);
                finish();
            }

        });
    }
    public void onBackPressed()
    {
        Intent i=new Intent(RulesActivity.this,MainActivity.class);
        startActivity(i);
        finish();
    }
}
