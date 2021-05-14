package in.thekites.quizlite;

import android.content.DialogInterface;
import android.content.Intent;
import android.graphics.Typeface;
import android.os.CountDownTimer;
import android.support.v7.app.ActionBar;
import android.support.v7.app.AlertDialog;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.view.Window;
import android.view.WindowManager;
import android.widget.Button;
import android.widget.ImageButton;
import android.widget.LinearLayout;
import android.widget.TextView;

import java.util.List;
import java.util.concurrent.TimeUnit;

public class quizAndroidhActivity extends AppCompatActivity implements View.OnClickListener{

    List<AndroidQuestion> quesList;
    int scoreAndroid = 0;
    int qid = 0;
    AndroidQuestion currentQ;
    TextView txtQuestion;
    TextView minute;

    Button opta, optb, optc;
    ImageButton back,home,close;
    int a=0,b=0,c=0;
    Button next;


    long timeRemaining=0;
    long timeTaken=0;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        getWindow().setFlags(WindowManager.LayoutParams.FLAG_FULLSCREEN,WindowManager.LayoutParams.FLAG_FULLSCREEN);
        requestWindowFeature(Window.FEATURE_NO_TITLE);
        ActionBar actionBar=getSupportActionBar();
        actionBar.hide();
        setContentView(R.layout.activity_quiz_android);

        DbHelperAndroidHard db = new DbHelperAndroidHard(this);
        quesList = db.getAllQuestions();
        currentQ = quesList.get(qid);

        txtQuestion = (TextView) findViewById(R.id.textview1);
        Typeface face=Typeface.createFromAsset(getAssets(), "fonts/Question.ttf");
        txtQuestion.setTypeface(face);
        minute=(TextView)findViewById(R.id.min);
        Typeface time=Typeface.createFromAsset(getAssets(), "fonts/time.ttf");
        minute.setTypeface(face);

        opta = (Button) findViewById(R.id.button_opta);
        optb = (Button) findViewById(R.id.button_optb);
        optc = (Button) findViewById(R.id.button_optc);

        Typeface face1=Typeface.createFromAsset(getAssets(), "fonts/Option.ttf");
        opta.setTypeface(face1);
        Typeface face2=Typeface.createFromAsset(getAssets(), "fonts/Option.ttf");
        optb.setTypeface(face2);
        Typeface face3=Typeface.createFromAsset(getAssets(), "fonts/Option.ttf");
        optc.setTypeface(face3);

        back=(ImageButton)findViewById(R.id.button_back);
        home=(ImageButton)findViewById(R.id.button_home);
        close=(ImageButton)findViewById(R.id.button_close);

        final LinearLayout layout=(LinearLayout)findViewById(R.id.layout1);
        final LinearLayout.LayoutParams layoutParams=new LinearLayout.LayoutParams(LinearLayout.LayoutParams.MATCH_PARENT,LinearLayout.LayoutParams.WRAP_CONTENT);
        layoutParams.setMargins(80,200,80,100);





        // button_next = (Button) findViewById(R.id.button1);

        new CountDownTimer(181000,1000) {


            @Override
            public void onTick(long millisUntilFinished) {

                minute.setText(""+String.format("%d min,%d sec", TimeUnit.MILLISECONDS.toMinutes(millisUntilFinished),
                        TimeUnit.MILLISECONDS.toSeconds(millisUntilFinished)-
                                TimeUnit.MINUTES.toSeconds(TimeUnit.MILLISECONDS.toMinutes(millisUntilFinished))));

                timeRemaining=millisUntilFinished;
                timeTaken=181000-timeRemaining;
                timeRemaining=timeRemaining/1000;
                timeTaken=timeTaken/1000;

            }

            @Override
            public void onFinish() {


            }
        }.start();


        opta.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {

                if(a==0) {
                    next = new Button(quizAndroidhActivity.this);
                    next.setText("Next");
                    next.setTextColor(getResources().getColor(R.color.changeOption2));
                    next.setOnClickListener(quizAndroidhActivity.this);

                    Typeface face=Typeface.createFromAsset(getAssets(),"fonts/comicbd.ttf");
                    next.setTypeface(face);

                    next.setLayoutParams(layoutParams);
                    next.setBackgroundResource(R.drawable.buttonshape7);
                    layout.addView(next);
                }
                a++;
                opta.setBackgroundResource(R.drawable.buttonshape);
                opta.setTextColor(getResources().getColor(R.color.changeOption4));
                System.out.print("Value of a="+a);
                optb.setEnabled(false);
                optc.setEnabled(false);

            }
        });
        optb.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if(b==0) {
                    next = new Button(quizAndroidhActivity.this);
                    next.setText("Next");
                    next.setTextColor(getResources().getColor(R.color.changeOption2));
                    next.setOnClickListener(quizAndroidhActivity.this);
                    next.setLayoutParams(layoutParams);
                    next.setBackgroundResource(R.drawable.buttonshape7);
                    Typeface face=Typeface.createFromAsset(getAssets(),"fonts/comicbd.ttf");
                    next.setTypeface(face);
                    layout.addView(next);
                }
                b++;
                optb.setBackgroundResource(R.drawable.buttonshape);
                optb.setTextColor(getResources().getColor(R.color.changeOption4));
                System.out.print("Value of b="+b);
                opta.setEnabled(false);
                optc.setEnabled(false);
            }
        });
        optc.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if(c==0) {
                    next = new Button(quizAndroidhActivity.this);
                    next.setText("Next");
                    next.setTextColor(getResources().getColor(R.color.changeOption2));
                    next.setOnClickListener(quizAndroidhActivity.this);
                    next.setLayoutParams(layoutParams);
                    next.setBackgroundResource(R.drawable.buttonshape7);
                    Typeface face=Typeface.createFromAsset(getAssets(),"fonts/comicbd.ttf");
                    next.setTypeface(face);
                    layout.addView(next);
                }
                c++;
                optc.setBackgroundResource(R.drawable.buttonshape);
                optc.setTextColor(getResources().getColor(R.color.changeOption4));
                System.out.print("Value of c="+c);
                optb.setEnabled(false);
                opta.setEnabled(false);
            }
        });

        back.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                AlertDialog.Builder builder=new AlertDialog.Builder(quizAndroidhActivity.this);
                builder.setMessage("Do you want to close the test?")
                        .setCancelable(false)
                        .setPositiveButton("Yes", new DialogInterface.OnClickListener() {
                            @Override
                            public void onClick(DialogInterface dialog, int which) {
                                Intent i=new Intent(quizAndroidhActivity.this,CategoryActivity.class);
                                startActivity(i);
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
                alert.setTitle("Closing the Test");
                alert.show();
            }
        });



        close.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                AlertDialog.Builder builder=new AlertDialog.Builder(quizAndroidhActivity.this);
                builder.setMessage("Do you want to close the test?")
                        .setCancelable(false)
                        .setPositiveButton("Yes", new DialogInterface.OnClickListener() {
                            @Override
                            public void onClick(DialogInterface dialog, int which) {
                                Intent i=new Intent(quizAndroidhActivity.this,ResultActivity.class);
                                startActivity(i);
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
                alert.setTitle("Closing the Test");
                alert.show();
            }
        });

        home.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                AlertDialog.Builder builder=new AlertDialog.Builder(quizAndroidhActivity.this);
                builder.setMessage("Do you want to go to Home?")
                        .setCancelable(false)
                        .setPositiveButton("Yes", new DialogInterface.OnClickListener() {
                            @Override
                            public void onClick(DialogInterface dialog, int which) {
                                Intent i=new Intent(quizAndroidhActivity.this,MainActivity.class);
                                startActivity(i);
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
                alert.setTitle("Returning Home");
                alert.show();
            }
        });

        setQuestionView();


    }
    public void onBackPressed()
    {

        AlertDialog.Builder builder=new AlertDialog.Builder(quizAndroidhActivity.this);
        builder.setMessage("Do you want to Exit the QuizLite?")
                .setCancelable(false)
                .setPositiveButton("Yes", new DialogInterface.OnClickListener() {
                    @Override
                    public void onClick(DialogInterface dialog, int which) {
                        moveTaskToBack(true);
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
        alert.setTitle("Exiting the QuizLite");
        alert.show();
    }


    private void setQuestionView() {
        txtQuestion.setText(currentQ.getQUESTION());
        opta.setText(currentQ.getOPTA());
        optb.setText(currentQ.getOPTB());
        optc.setText(currentQ.getOPTC());
        qid++;

    }

    @Override
    public void onClick(View v) {


      /* if(opta.isEnabled())
       {
           a=0;
           opta.setBackgroundResource(R.drawable.buttonshapeA);
           optb.setEnabled(true);
           optc.setEnabled(true);
           LinearLayout layout=(LinearLayout)findViewById(R.id.layout1);
           LinearLayout.LayoutParams layoutParams=new LinearLayout.LayoutParams(LinearLayout.LayoutParams.MATCH_PARENT,LinearLayout.LayoutParams.WRAP_CONTENT);
           layout.removeView(next);


       }
        if(optb.isEnabled())
        {
            b=0;
            optb.setBackgroundResource(R.drawable.buttonshapeA);
            opta.setEnabled(true);
            optc.setEnabled(true);
            LinearLayout layout=(LinearLayout)findViewById(R.id.layout1);
            LinearLayout.LayoutParams layoutParams=new LinearLayout.LayoutParams(LinearLayout.LayoutParams.MATCH_PARENT,LinearLayout.LayoutParams.WRAP_CONTENT);

            layout.removeView(next);
        }
        if(optc.isEnabled())
        {
            c=0;
            optc.setBackgroundResource(R.drawable.buttonshapeA);
            optb.setEnabled(true);
            opta.setEnabled(true);
            LinearLayout layout=(LinearLayout)findViewById(R.id.layout1);
            LinearLayout.LayoutParams layoutParams=new LinearLayout.LayoutParams(LinearLayout.LayoutParams.MATCH_PARENT,LinearLayout.LayoutParams.WRAP_CONTENT);

            layout.removeView(next);
        }*/


        if (opta.isEnabled()||a==1||a>1) {
            a=0;
            opta.setBackgroundResource(R.drawable.buttonshapeb);
            opta.setTextColor(getResources().getColor(R.color.changeOption2));
            optb.setEnabled(true);
            optc.setEnabled(true);
            LinearLayout layout=(LinearLayout)findViewById(R.id.layout1);
            LinearLayout.LayoutParams layoutParams=new LinearLayout.LayoutParams(LinearLayout.LayoutParams.MATCH_PARENT,LinearLayout.LayoutParams.WRAP_CONTENT);
            layout.removeView(next);

            String answer = opta.getText().toString();

            if(currentQ.getANSWER().equals(answer))
            {
                scoreAndroid++;
                Log.d("score","Your Score:"+scoreAndroid);
            }
            if(qid<5&&timeRemaining!=0)
            {
                currentQ=quesList.get(qid);
                setQuestionView();
            }
            else
            {
                Intent intent=new Intent(this,ResultHardActivity.class);
                String score_string=String.valueOf(scoreAndroid);
                intent.putExtra("scoreAndroid",score_string);
                intent.putExtra("timeRemaining",timeRemaining);
                intent.putExtra("timeTaken",timeTaken);
                startActivity(intent);

            }
        }

        else if(optb.isEnabled()||b==1||b>1)
        {
            b=0;
            optb.setBackgroundResource(R.drawable.buttonshapeb);
            optb.setTextColor(getResources().getColor(R.color.changeOption2));
            opta.setEnabled(true);
            optc.setEnabled(true);
            LinearLayout layout=(LinearLayout)findViewById(R.id.layout1);
            LinearLayout.LayoutParams layoutParams=new LinearLayout.LayoutParams(LinearLayout.LayoutParams.MATCH_PARENT,LinearLayout.LayoutParams.WRAP_CONTENT);

            layout.removeView(next);

            String answer=optb.getText().toString();

            if(currentQ.getANSWER().equals(answer))
            {
                scoreAndroid++;
                Log.d("score","Your Score:"+scoreAndroid);
            }
            if(qid<5&&timeRemaining!=0)
            {
                currentQ=quesList.get(qid);
                setQuestionView();
            }
            else
            {
                Intent intent=new Intent(this,ResultHardActivity.class);
                String score_string=String.valueOf(scoreAndroid);
                intent.putExtra("scoreAndroid",score_string);
                intent.putExtra("timeRemaining",timeRemaining);
                intent.putExtra("timeTaken",timeTaken);
                startActivity(intent);

            }
        }
        else if(optc.isEnabled()||c==1||c>1)
        {
            c=0;
            optc.setBackgroundResource(R.drawable.buttonshapeb);
            optc.setTextColor(getResources().getColor(R.color.changeOption2));
            optb.setEnabled(true);
            opta.setEnabled(true);
            LinearLayout layout=(LinearLayout)findViewById(R.id.layout1);
            LinearLayout.LayoutParams layoutParams=new LinearLayout.LayoutParams(LinearLayout.LayoutParams.MATCH_PARENT,LinearLayout.LayoutParams.WRAP_CONTENT);

            layout.removeView(next);

            String answer=optc.getText().toString();

            if(currentQ.getANSWER().equals(answer))
            {
                scoreAndroid++;
                Log.d("score","Your Score:"+scoreAndroid);
            }
            if(qid<5&&timeRemaining!=0)
            {
                currentQ=quesList.get(qid);
                setQuestionView();
            }
            else
            {
                Intent intent=new Intent(this,ResultHardActivity.class);
                String score_string=String.valueOf(scoreAndroid);
                intent.putExtra("scoreAndroid",score_string);
                intent.putExtra("timeRemaining",timeRemaining);
                intent.putExtra("timeTaken",timeTaken);
                startActivity(intent);

            }
        }
    }
}
