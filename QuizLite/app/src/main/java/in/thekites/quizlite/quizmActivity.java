package in.thekites.quizlite;

import android.content.DialogInterface;
import android.content.Intent;
import android.graphics.Typeface;
import android.os.CountDownTimer;
import android.support.v7.app.ActionBar;
import android.support.v7.app.AlertDialog;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.view.ViewGroup;
import android.view.Window;
import android.view.WindowManager;
import android.widget.Button;
import android.widget.ImageButton;
import android.widget.LinearLayout;
import android.widget.RelativeLayout;
import android.widget.TextView;

import java.util.List;
import java.util.concurrent.TimeUnit;


public class quizmActivity extends AppCompatActivity implements View.OnClickListener {

    List<Question> quesList;
    int scorec = 0;
    int qid = 0;
    Question currentQ;
    TextView txtQuestion;

    TextView minute;

    Button opta, optb, optc;
    ImageButton back,home,close;
    int a = 0, b = 0, c = 0;
    Button next;
    int min,sec;
    int delay=1000;

    long timeRemaining=0;
    long timeTaken=0;

//    RelativeLayout r1=(RelativeLayout)findViewById(R.id.r1);
    //  RelativeLayout.LayoutParams yparams=new RelativeLayout.LayoutParams(900,120);

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        getWindow().setFlags(WindowManager.LayoutParams.FLAG_FULLSCREEN,WindowManager.LayoutParams.FLAG_FULLSCREEN);
        requestWindowFeature(Window.FEATURE_NO_TITLE);
        ActionBar actionBar=getSupportActionBar();
        actionBar.hide();
        setContentView(R.layout.activity_quiz);
        minute=(TextView)findViewById(R.id.min);



        DbHelperMedium db = new DbHelperMedium(this);
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


        final LinearLayout layout = (LinearLayout) findViewById(R.id.layout1);
        final LinearLayout.LayoutParams layoutParams = new LinearLayout.LayoutParams(LinearLayout.LayoutParams.MATCH_PARENT, LinearLayout.LayoutParams.WRAP_CONTENT);
        layoutParams.setMargins(80,200,80,0);


        // button_next = (Button) findViewById(R.id.button1);
        /*for(min=3;min>0;min--)
        {
            minute.setText(String.valueOf(min));
            for(sec=59;sec>0;sec--)
            {
                try
                {
                    minute.setText(String.valueOf(min-1));
                    second.setText(String.valueOf(sec));
                    Thread.sleep(1000);
                }
                catch (Exception ex)
                {

                }
            }
        }*/
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

                if (a == 0) {
                    next = new Button(quizmActivity.this);
                    next.setText("Next");
                    next.setTextColor(getResources().getColor(R.color.changeOption2));
                    next.setOnClickListener(quizmActivity.this);

                    Typeface face=Typeface.createFromAsset(getAssets(),"fonts/comicbd.ttf");
                    next.setTypeface(face);

                    /*RelativeLayout.LayoutParams params=new RelativeLayout.LayoutParams(900,120);
                    params.addRule(RelativeLayout.ALIGN_PARENT_BOTTOM,RelativeLayout.TRUE);
                    params.setMargins(0,0,20,60);

                    RelativeLayout.LayoutParams xparams=new RelativeLayout.LayoutParams(RelativeLayout.LayoutParams.WRAP_CONTENT,RelativeLayout.LayoutParams.WRAP_CONTENT);
                   xparams.addRule(RelativeLayout.CENTER_HORIZONTAL,RelativeLayout.TRUE);
                    xparams.addRule(RelativeLayout.ABOVE,R.id.downbar);*/
                    //xparams.addRule(RelativeLayout.BELOW,R.id.button_optc);



                    //yparams.bottomMargin=500;
                    // params.addRule(RelativeLayout.BELOW,R.id.button_optc);

                    next.setLayoutParams(layoutParams);
                    next.setBackgroundResource(R.drawable.buttonshape7);
                    layout.addView(next);
                    // r1.addView(next,yparams);
                }
                a++;
                opta.setBackgroundResource(R.drawable.buttonshape);
                opta.setTextColor(getResources().getColor(R.color.changeOption1));
                System.out.print("Value of a=" + a);
                optb.setEnabled(false);
                optc.setEnabled(false);

            }
        });
        optb.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if (b == 0) {
                    next = new Button(quizmActivity.this);
                    next.setText("Next");
                    next.setTextColor(getResources().getColor(R.color.changeOption2));
                    next.setOnClickListener(quizmActivity.this);
                    next.setLayoutParams(layoutParams);
                    next.setBackgroundResource(R.drawable.buttonshape7);
                    Typeface face=Typeface.createFromAsset(getAssets(),"fonts/comicbd.ttf");
                    next.setTypeface(face);
                    layout.addView(next);
                }
                b++;
                optb.setBackgroundResource(R.drawable.buttonshape);
                optb.setTextColor(getResources().getColor(R.color.changeOption1));
                System.out.print("Value of b=" + b);
                opta.setEnabled(false);
                optc.setEnabled(false);
            }
        });
        optc.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if (c == 0) {
                    next = new Button(quizmActivity.this);
                    next.setText("Next");
                    next.setTextColor(getResources().getColor(R.color.changeOption2));
                    next.setOnClickListener(quizmActivity.this);
                    next.setLayoutParams(layoutParams);
                    next.setBackgroundResource(R.drawable.buttonshape7);
                    Typeface face=Typeface.createFromAsset(getAssets(),"fonts/comicbd.ttf");
                    next.setTypeface(face);
                    layout.addView(next);
                }
                c++;
                optc.setBackgroundResource(R.drawable.buttonshape);
                optc.setTextColor(getResources().getColor(R.color.changeOption1));
                System.out.print("Value of c=" + c);
                optb.setEnabled(false);
                opta.setEnabled(false);
            }
        });

        back.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                AlertDialog.Builder builder=new AlertDialog.Builder(quizmActivity.this);
                builder.setMessage("Do you want to close the test?")
                        .setCancelable(false)
                        .setPositiveButton("Yes", new DialogInterface.OnClickListener() {
                            @Override
                            public void onClick(DialogInterface dialog, int which) {
                                Intent i=new Intent(quizmActivity.this,CategoryActivity.class);
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
                AlertDialog.Builder builder=new AlertDialog.Builder(quizmActivity.this);
                builder.setMessage("Do you want to close the test?")
                        .setCancelable(false)
                        .setPositiveButton("Yes", new DialogInterface.OnClickListener() {
                            @Override
                            public void onClick(DialogInterface dialog, int which) {
                                Intent i=new Intent(quizmActivity.this,ResultActivity.class);
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
                AlertDialog.Builder builder=new AlertDialog.Builder(quizmActivity.this);
                builder.setMessage("Do you want to go to Home?")
                        .setCancelable(false)
                        .setPositiveButton("Yes", new DialogInterface.OnClickListener() {
                            @Override
                            public void onClick(DialogInterface dialog, int which) {
                                Intent i=new Intent(quizmActivity.this,MainActivity.class);
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

        AlertDialog.Builder builder=new AlertDialog.Builder(quizmActivity.this);
        builder.setMessage("Do you want to Exit the QuizLite?")
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

       /* String score_string=String.valueOf(score);
        txt2.setText(score_string);*/
        //qid++;
        /*if (qid < 5) {
            currentQ = quesList.get(qid);
            setQuestionView();
        } else {
            String score_string = String.valueOf(score);
            try{
            txt2.setText(score_string);
            Thread.sleep(3000);}
            catch(Exception e){}

           Intent intent = new Intent(this, ResultActivity.class);
            String score_string = String.valueOf(score);
            intent.putExtra("score", score_string);
            startActivity(intent);

        }*/

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


        if (opta.isEnabled() || a == 1 || a > 1) {
            a = 0;
            opta.setBackgroundResource(R.drawable.buttonshapea);
            opta.setTextColor(getResources().getColor(R.color.changeOption2));
            optb.setEnabled(true);
            optc.setEnabled(true);
            LinearLayout layout = (LinearLayout) findViewById(R.id.layout1);
            // LinearLayout.LayoutParams layoutParams = new LinearLayout.LayoutParams(LinearLayout.LayoutParams.MATCH_PARENT, LinearLayout.LayoutParams.WRAP_CONTENT);
            layout.removeView(next);
            // r1.removeView(yparams);


            String answer = opta.getText().toString();


            if (currentQ.getANSWER().equalsIgnoreCase(answer)) {
                scorec++;

                //Log.d("score","Your Score:"+score);
                String s = String.valueOf(scorec);
                // txt2=new TextView(quizActivity.this);



            }

            if(qid<5&&timeRemaining!=0)
            {
                currentQ=quesList.get(qid);
                setQuestionView();
            }
            else
            {
                Intent intent=new Intent(this,ResultMediumActivity.class);
                String score_string=String.valueOf(scorec);
                intent.putExtra("scorec",score_string);
                intent.putExtra("timeRemaining",timeRemaining);
                intent.putExtra("timeTaken",timeTaken);
                startActivity(intent);


            }
        } else if (optb.isEnabled() || b == 1 || b > 1) {
            b = 0;
            optb.setBackgroundResource(R.drawable.buttonshapea);
            optb.setTextColor(getResources().getColor(R.color.changeOption2));
            opta.setEnabled(true);
            optc.setEnabled(true);
            LinearLayout layout = (LinearLayout) findViewById(R.id.layout1);
            LinearLayout.LayoutParams layoutParams = new LinearLayout.LayoutParams(LinearLayout.LayoutParams.MATCH_PARENT, LinearLayout.LayoutParams.WRAP_CONTENT);

            layout.removeView(next);


            String answer = optb.getText().toString();


            if (currentQ.getANSWER().equalsIgnoreCase(answer)) {
                scorec++;
                // Log.d("score","Your Score:"+score);
                String s = String.valueOf(scorec);
                //txt2=new TextView(quizActivity.this);

            }
            if(qid<5&&timeRemaining!=0)
            {
                currentQ=quesList.get(qid);
                setQuestionView();
            }
            else
            {
                Intent intent=new Intent(this,ResultMediumActivity.class);
                String score_string=String.valueOf(scorec);

                intent.putExtra("scorec",score_string);
                intent.putExtra("timeRemaining",timeRemaining);
                intent.putExtra("timeTaken",timeTaken);

                startActivity(intent);


            }
        } else if (optc.isEnabled() || c == 1 || c > 1) {
            c = 0;
            optc.setBackgroundResource(R.drawable.buttonshapea);
            optc.setTextColor(getResources().getColor(R.color.changeOption2));
            optb.setEnabled(true);
            opta.setEnabled(true);
            LinearLayout layout = (LinearLayout) findViewById(R.id.layout1);
            LinearLayout.LayoutParams layoutParams = new LinearLayout.LayoutParams(LinearLayout.LayoutParams.MATCH_PARENT, LinearLayout.LayoutParams.WRAP_CONTENT);

            layout.removeView(next);


            String answer = optc.getText().toString();


            if (currentQ.getANSWER().equalsIgnoreCase(answer)) {
                scorec++;
                //Log.d("score","Your Score:"+score);
                String s = String.valueOf(scorec);
                //  txt2=new TextView(quizActivity.this);

            }
            if(qid<5&&timeRemaining!=0)
            {
                currentQ=quesList.get(qid);
                setQuestionView();
            }
            else
            {
                Intent intent=new Intent(this,ResultMediumActivity.class);
                String score_string=String.valueOf(scorec);

                intent.putExtra("scorec",score_string);
                intent.putExtra("timeRemaining",timeRemaining);
                intent.putExtra("timeTaken",timeTaken);


                startActivity(intent);



            }
        }

    }
}
