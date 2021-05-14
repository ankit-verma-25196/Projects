package in.thekites.quizlite;

import android.content.Intent;
import android.support.v7.app.ActionBar;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.view.Window;
import android.view.WindowManager;
import android.widget.Button;
import android.widget.ImageButton;
import android.widget.Toast;

public class LevelAndroidActivity extends AppCompatActivity {

    ImageButton back,home,close;

    Button easy,medium,hard;
    //int scoreAndroidint,scoreAndroidmint;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        getWindow().setFlags(WindowManager.LayoutParams.FLAG_FULLSCREEN,WindowManager.LayoutParams.FLAG_FULLSCREEN);
        requestWindowFeature(Window.FEATURE_NO_TITLE);
        ActionBar actionBar=getSupportActionBar();
        actionBar.hide();
        setContentView(R.layout.activity_level_android);

        back=(ImageButton)findViewById(R.id.button_back);
        home=(ImageButton)findViewById(R.id.button_home);
        close=(ImageButton)findViewById(R.id.button_close);

        easy=(Button)findViewById(R.id.button_easy);
        medium=(Button)findViewById(R.id.button_medium);
        hard=(Button)findViewById(R.id.button_hard);

      /*  Intent in=getIntent();
        String scoreAndroid=in.getStringExtra("scoreAndroid");
        String scoreAndroidm=in.getStringExtra("scoreAndroidm");

        scoreAndroidint=Integer.parseInt(scoreAndroid);
        scoreAndroidmint=Integer.parseInt(scoreAndroidm);*/




        back.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {

                Intent i=new Intent(LevelAndroidActivity.this,CategoryActivity.class);
                startActivity(i);
                finish();

            }


        });
        home.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {

                Intent i=new Intent(LevelAndroidActivity.this,MainActivity.class);
                startActivity(i);
                finish();

            }


        });


    }

    public void easy(View view)
    {
        Intent i=new Intent(LevelAndroidActivity.this,quizAndroidActivity.class);
        startActivity(i);
        finish();
    }

    public void medium(View view)
    {

            Intent i=new Intent(LevelAndroidActivity.this,quizAndroidmActivity.class);
            startActivity(i);
            finish();


    }

    public void hard(View view)
    {

            Intent i=new Intent(LevelAndroidActivity.this,quizAndroidhActivity.class);
            startActivity(i);
            finish();
    }

    public void onBackPressed()
    {
        Intent i=new Intent(LevelAndroidActivity.this,CategoryActivity.class);
        startActivity(i);
        finish();
    }

}
