package in.thekites.quizlite;

import android.content.DialogInterface;
import android.content.Intent;
import android.os.AsyncTask;
import android.support.v7.app.ActionBar;
import android.support.v7.app.AlertDialog;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.view.Window;
import android.view.WindowManager;
import android.view.animation.Animation;
import android.view.animation.AnimationUtils;
import android.widget.Button;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity  {

    Button button_start,button_rules,button_exit;



    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        getWindow().setFlags(WindowManager.LayoutParams.FLAG_FULLSCREEN,WindowManager.LayoutParams.FLAG_FULLSCREEN);
        requestWindowFeature(Window.FEATURE_NO_TITLE);
        ActionBar actionBar=getSupportActionBar();
        actionBar.hide();

        setContentView(R.layout.activity_main);

       button_start = (Button) findViewById(R.id.button_start);
        button_rules = (Button) findViewById(R.id.bt_rules);
        button_exit = (Button) findViewById(R.id.bt_exit);



        button_start.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent in=new Intent(MainActivity.this,CategoryActivity.class);
                startActivity(in);
                finish();
            }
        });
        button_exit.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {

                AlertDialog.Builder builder=new AlertDialog.Builder(MainActivity.this);
                builder.setMessage("Do you want to Exit the QuizLite")
                        .setCancelable(false)
                        .setPositiveButton("Yes", new DialogInterface.OnClickListener() {
                            @Override
                            public void onClick(DialogInterface dialog, int which) {
                                moveTaskToBack(false);
                                android.os.Process.killProcess(android.os.Process.myPid());
                                System.exit(1);
                                //finish();
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
        });

       button_rules.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent i=new Intent(MainActivity.this,RulesActivity.class);
                startActivity(i);
                finish();
            }
        });

    }

    public void onBackPressed()
    {
        Toast.makeText(MainActivity.this,"Action not Allowed",Toast.LENGTH_SHORT);
    }
   /* @Override
    public void onClick(View v) {

        if(v==button_start)
        {
            Animation myAnim=AnimationUtils.loadAnimation(getApplicationContext(),R.anim.milkshake);
            button_start.startAnimation(myAnim);

        }
        else if(v==button_rules)
        {
            Animation myAnim=AnimationUtils.loadAnimation(getApplicationContext(),R.anim.milkshake);
            v.startAnimation(myAnim);
        }
        else if(v==button_exit)
        {
            Animation myAnim=AnimationUtils.loadAnimation(getApplicationContext(),R.anim.milkshake);
            v.startAnimation(myAnim);
        }


    }*/





/*
    class myAsyncTask extends AsyncTask<Void,Void,Void>{


        protected void onPostExecute(Void aVoid) {
            super.onPostExecute(aVoid);



                    }

        @Override
        protected Void doInBackground(Void... params) {

            return null;
        }
    }*/

}
