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

public class LevelJavaActivity extends AppCompatActivity {

    ImageButton back,home,close;

    Button easy,medium,hard;

   // int scoreJavaint,scoreJavamint;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        getWindow().setFlags(WindowManager.LayoutParams.FLAG_FULLSCREEN,WindowManager.LayoutParams.FLAG_FULLSCREEN);
        requestWindowFeature(Window.FEATURE_NO_TITLE);
        ActionBar actionBar=getSupportActionBar();
        actionBar.hide();
        setContentView(R.layout.activity_level_java);

        back=(ImageButton)findViewById(R.id.button_back);
        home=(ImageButton)findViewById(R.id.button_home);
        close=(ImageButton)findViewById(R.id.button_close);

        easy=(Button)findViewById(R.id.button_easy);
        medium=(Button)findViewById(R.id.button_medium);
        hard=(Button)findViewById(R.id.button_hard);

     /*   Intent in=getIntent();
        String scoreJava=in.getStringExtra("scoreJava");
        String scoreJavam=in.getStringExtra("scoreJavam");

        scoreJavaint=Integer.parseInt(scoreJava);
        scoreJavamint=Integer.parseInt(scoreJavam);*/



        back.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {

                Intent i=new Intent(LevelJavaActivity.this,CategoryActivity.class);
                startActivity(i);
                finish();

            }


        });
        home.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {

                Intent i=new Intent(LevelJavaActivity.this,MainActivity.class);
                startActivity(i);
                finish();

            }


        });


    }

    public void easy(View view)
    {
        Intent i=new Intent(LevelJavaActivity.this,quizJavaActivity.class);
        startActivity(i);
        finish();
    }

    public void medium(View view)
    {
            Intent i=new Intent(LevelJavaActivity.this,quizJavamActivity.class);
            startActivity(i);
            finish();


    }

    public void hard(View view)
    {

            Intent i=new Intent(LevelJavaActivity.this,quizJavahActivity.class);
            startActivity(i);
            finish();
    }

    public void onBackPressed()
    {
        Intent i=new Intent(LevelJavaActivity.this,CategoryActivity.class);
        startActivity(i);
        finish();
    }
}
