package in.thekites.quizlite;

import android.content.DialogInterface;
import android.content.Intent;
import android.graphics.Typeface;
import android.support.v7.app.ActionBar;
import android.support.v7.app.AlertDialog;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.view.Window;
import android.view.WindowManager;
import android.widget.Button;

public class CategoryActivity extends AppCompatActivity {

    Button rules, exit;
    Button c, java, android;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        getWindow().setFlags(WindowManager.LayoutParams.FLAG_FULLSCREEN,WindowManager.LayoutParams.FLAG_FULLSCREEN);
        requestWindowFeature(Window.FEATURE_NO_TITLE);
        ActionBar actionBar=getSupportActionBar();
        actionBar.hide();
        setContentView(R.layout.activity_category);
        rules = (Button) findViewById(R.id.bt_rules);
        Typeface face = Typeface.createFromAsset(getAssets(), "fonts/ARDESTINE.ttf");
        rules.setTypeface(face);
        c = (Button) findViewById(R.id.bt_c);
        java = (Button) findViewById(R.id.bt_java);
        android = (Button) findViewById(R.id.bt_android);

        c.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent in = new Intent(CategoryActivity.this, LevelActivity.class);
                startActivity(in);
                finish();
            }
        });
        java.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent in = new Intent(CategoryActivity.this, LevelJavaActivity.class);
                startActivity(in);
                finish();
            }
        });
        android.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent in = new Intent(CategoryActivity.this, LevelAndroidActivity.class);
                startActivity(in);
                finish();
            }
        });

       /* exit.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {

                AlertDialog.Builder builder=new AlertDialog.Builder(CategoryActivity.this);
                builder.setMessage("Do you want to Exit the QuizLite?")
                        .setCancelable(false)
                        .setPositiveButton("Yes", new DialogInterface.OnClickListener() {
                            @Override
                            public void onClick(DialogInterface dialog, int which) {
                               moveTaskToBack(false);
                                //android.os.Process.killProcess(android.os.Process.myPid());
                                //System.exit(1);
                                finish();
                            }
                        })
                        .setNegativeButton("No", new DialogInterface.OnClickListener() {
                            @Override
                            public void onClick(DialogInterface dialog, int which) {
                                dialog.cancel();
                            }
                        });

                AlertDialog alert=builder.create();
                alert.setTitle("Exiting the App");
                alert.show();
                        }
        });*/
        rules.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent i=new Intent(CategoryActivity.this,RulesActivity.class);
                startActivity(i);
                finish();
            }
        });


    }


    public void onBackPressed()
    {
        Intent i=new Intent(CategoryActivity.this,MainActivity.class);
        startActivity(i);
        finish();
    }
}


