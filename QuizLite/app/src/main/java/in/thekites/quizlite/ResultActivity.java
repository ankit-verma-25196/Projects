package in.thekites.quizlite;

import android.content.DialogInterface;
import android.content.Intent;
import android.support.v7.app.ActionBar;
import android.support.v7.app.AlertDialog;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.view.Window;
import android.view.WindowManager;
import android.widget.ImageButton;
import android.widget.RatingBar;
import android.widget.TabHost;
import android.widget.TextView;

import java.util.concurrent.TimeUnit;

public class ResultActivity extends AppCompatActivity {

    String scorec,scoreJava,scoreAndroid;
   // static ResultActivity INSTANCE;


    ImageButton restart,home,close;
    ImageButton restartj,homej,closej;
    ImageButton restarta,homea,closea;

    TabHost tabHost;
    TextView text1,text2,text3,text4,text5,text6;
    TextView txt1,txt2,txt3,txt4,txt5,txt6;
    TextView tx1,tx2,tx3,tx4,tx5,tx6;
    long cTaken=0,cRemaining=0,remTaken=0,remRemaining=0;
    long cJavaTaken=0,cJavaRemaining=0,remJavaTaken=0,remJavaRemaining=0;
    long cAndroidTaken=0,cAndroidRemaining=0,remAndroidTaken=0,remAndroidRemaining=0;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
     //   INSTANCE=this;
        super.onCreate(savedInstanceState);
        getWindow().setFlags(WindowManager.LayoutParams.FLAG_FULLSCREEN,WindowManager.LayoutParams.FLAG_FULLSCREEN);
        requestWindowFeature(Window.FEATURE_NO_TITLE);
        ActionBar actionBar=getSupportActionBar();
        actionBar.hide();
        setContentView(R.layout.activity_result);



        tabHost=(TabHost)findViewById(R.id.tabhost);
        tabHost.setup();

        TabHost.TabSpec tab=tabHost.newTabSpec("A");
        tab.setContent(R.id.cplusplus);
        tab.setIndicator("C++");
       /* for(int tabIndex=0;tabIndex  <tabHost.getTabWidget().getTabCount();tabIndex++)
        {
            View tabb=tabHost.getTabWidget().getChildTabViewAt(tabIndex);
            TextView t=(TextView)tabb.findViewById(android.R.id.title);
            t.setTextColor(getResources().getColor(R.color.changeOption2));
        }*/
        tabHost.addTab(tab);

        tab=tabHost.newTabSpec("B");
        tab.setContent(R.id.java);
        tab.setIndicator("Java");
        tabHost.addTab(tab);

        tab=tabHost.newTabSpec("C");
        tab.setContent(R.id.android);
        tab.setIndicator("Android");
        tabHost.addTab(tab);


        text1=(TextView)findViewById(R.id.text1);
        text2=(TextView)findViewById(R.id.text2);
        text3=(TextView)findViewById(R.id.text3);
        text4=(TextView)findViewById(R.id.text4);
        text5=(TextView)findViewById(R.id.text5);
        text6=(TextView)findViewById(R.id.text6);

        txt1=(TextView)findViewById(R.id.txt1);
        txt2=(TextView)findViewById(R.id.txt2);
        txt3=(TextView)findViewById(R.id.txt3);
        txt4=(TextView)findViewById(R.id.txt4);
        txt5=(TextView)findViewById(R.id.txt5);
        txt6=(TextView)findViewById(R.id.txt6);

        tx1=(TextView)findViewById(R.id.tx1);
        tx2=(TextView)findViewById(R.id.tx2);
        tx3=(TextView)findViewById(R.id.tx3);
        tx4=(TextView)findViewById(R.id.tx4);
        tx5=(TextView)findViewById(R.id.tx5);
        tx6=(TextView)findViewById(R.id.tx6);

        restart=(ImageButton)findViewById(R.id.button_restart);
        home=(ImageButton)findViewById(R.id.button_home);
        close=(ImageButton)findViewById(R.id.button_close);

        restartj=(ImageButton)findViewById(R.id.button_restartj);
        homej=(ImageButton)findViewById(R.id.button_homej);
        closej=(ImageButton)findViewById(R.id.button_closej);

        restarta=(ImageButton)findViewById(R.id.button_restarta);
        homea=(ImageButton)findViewById(R.id.button_homea);
        closea=(ImageButton)findViewById(R.id.button_closea);


        Intent in=getIntent();

         scorec=in.getStringExtra("scorec");
        long timeTakenCLong=in.getLongExtra("timeTaken",0);
        long timeRemainingCLong=in.getLongExtra("timeRemaining",0);

       /* Intent intent1=new Intent(this,LevelActivity.class);
        intent1.putExtra("scorec",scorec);*/

        remTaken=timeTakenCLong%60;
        while(timeTakenCLong>=60)
        {
            timeTakenCLong=timeTakenCLong-60;
            cTaken++;
        }

        remRemaining=timeRemainingCLong%60;
        while(timeRemainingCLong>=60)
        {
            timeRemainingCLong=timeRemainingCLong-60;
            cRemaining++;
        }



         scoreJava=in.getStringExtra("scoreJava");
        long timeTakenJavaLong=in.getLongExtra("timeTaken",0);
        long timeRemainingJavaLong=in.getLongExtra("timeRemaining",0);

       /* Intent intent2=new Intent(this,LevelJavaActivity.class);
        intent2.putExtra("scoreJava",scoreJava);*/


        remJavaTaken=timeTakenJavaLong%60;
        while(timeTakenJavaLong>=60)
        {
            timeTakenJavaLong=timeTakenJavaLong-60;
            cJavaTaken++;
        }

        remJavaRemaining=timeRemainingJavaLong%60;
        while(timeRemainingJavaLong>=60)
        {
            timeRemainingJavaLong=timeRemainingJavaLong-60;
            cJavaRemaining++;
        }


         scoreAndroid=in.getStringExtra("scoreAndroid");
        long timeTakenAndroidLong=in.getLongExtra("timeTaken",0);
        long timeRemainingAndroidLong=in.getLongExtra("timeRemaining",0);

       /* Intent intent3=new Intent(this,LevelAndroidActivity.class);
        intent3.putExtra("scoreAndroid",scoreAndroid);*/



        remAndroidTaken=timeTakenAndroidLong%60;
        while(timeTakenAndroidLong>=60)
        {
            timeTakenAndroidLong=timeTakenAndroidLong-60;
            cAndroidTaken++;
        }

        remAndroidRemaining=timeRemainingAndroidLong%60;
        while(timeRemainingAndroidLong>=60)
        {
            timeRemainingAndroidLong=timeRemainingAndroidLong-60;
            cAndroidRemaining++;
        }


        // int scoreInt=Integer.parseInt(score);

if(scorec!=null) {
    switch (scorec) {
        case "0":
            text2.setText(scorec);
           /* text4.setText(""+String.format("%d min,%d sec", TimeUnit.MILLISECONDS.toMinutes(timeTakenCLong),
                    TimeUnit.MILLISECONDS.toSeconds(timeTakenCLong)-
                    TimeUnit.MINUTES.toSeconds(TimeUnit.MILLISECONDS.toMinutes(timeTakenCLong))));*/
            if(remTaken<10) {
               String cTakenString=String.valueOf(cTaken);
                String remTakenString=String.valueOf(remTaken);
                text4.setText("0"+cTakenString+" min,"+"0"+remTakenString+" sec");
            }
            else
            {
                String cTakenString=String.valueOf(cTaken);
                String remTakenString=String.valueOf(remTaken);
                text4.setText("0"+cTakenString+" min,"+remTakenString+" sec");
            }
            /*text6.setText(""+String.format("%d min,%d sec", TimeUnit.MILLISECONDS.toMinutes(timeRemainingCLong),
                    TimeUnit.MILLISECONDS.toSeconds(timeRemainingCLong)-
                            TimeUnit.MINUTES.toSeconds(TimeUnit.MILLISECONDS.toMinutes(timeRemainingCLong))));*/
            if(remRemaining<10) {
                String cTakenString=String.valueOf(cRemaining);
                String remRemainingString=String.valueOf(remRemaining);
                text6.setText("0"+cTakenString+" min,"+"0"+remRemainingString+" sec");
            }
            else
            {
                String cTakenString=String.valueOf(cRemaining);
                String remRemainingString=String.valueOf(remRemaining);
                text6.setText("0"+cTakenString+" min,"+remRemainingString+" sec");
            }

            break;
        case "1":

            text2.setText(scorec);
            /*text4.setText(""+String.format("%d min,%d sec", TimeUnit.MILLISECONDS.toMinutes(timeTakenCLong),
                    TimeUnit.MILLISECONDS.toSeconds(timeTakenCLong)-
                            TimeUnit.MINUTES.toSeconds(TimeUnit.MILLISECONDS.toMinutes(timeTakenCLong))));
            text6.setText(""+String.format("%d min,%d sec", TimeUnit.MILLISECONDS.toMinutes(timeRemainingCLong),
                    TimeUnit.MILLISECONDS.toSeconds(timeRemainingCLong)-
                            TimeUnit.MINUTES.toSeconds(TimeUnit.MILLISECONDS.toMinutes(timeRemainingCLong))));*/
            if(remTaken<10) {
                String cTakenString=String.valueOf(cTaken);
                String remTakenString=String.valueOf(remTaken);
                text4.setText("0"+cTakenString+" min,"+"0"+remTakenString+" sec");
            }
            else
            {
                String cTakenString=String.valueOf(cTaken);
                String remTakenString=String.valueOf(remTaken);
                text4.setText("0"+cTakenString+" min,"+remTakenString+" sec");
            }

            if(remRemaining<10) {
                String cTakenString=String.valueOf(cRemaining);
                String remRemainingString=String.valueOf(remRemaining);
                text6.setText("0"+cTakenString+" min,"+"0"+remRemainingString+" sec");
            }
            else
            {
                String cTakenString=String.valueOf(cRemaining);
                String remRemainingString=String.valueOf(remRemaining);
                text6.setText("0"+cTakenString+" min,"+remRemainingString+" sec");
            }

            break;
        case "2":

            text2.setText(scorec);
          /*  text4.setText(""+String.format("%d min,%d sec", TimeUnit.MILLISECONDS.toMinutes(timeTakenCLong),
                    TimeUnit.MILLISECONDS.toSeconds(timeTakenCLong)-
                            TimeUnit.MINUTES.toSeconds(TimeUnit.MILLISECONDS.toMinutes(timeTakenCLong))));
            text6.setText(""+String.format("%d min,%d sec", TimeUnit.MILLISECONDS.toMinutes(timeRemainingCLong),
                    TimeUnit.MILLISECONDS.toSeconds(timeRemainingCLong)-
                            TimeUnit.MINUTES.toSeconds(TimeUnit.MILLISECONDS.toMinutes(timeRemainingCLong))));*/
            if(remTaken<10) {
                String cTakenString=String.valueOf(cTaken);
                String remTakenString=String.valueOf(remTaken);
                text4.setText("0"+cTakenString+" min,"+"0"+remTakenString+" sec");
            }
            else
            {
                String cTakenString=String.valueOf(cTaken);
                String remTakenString=String.valueOf(remTaken);
                text4.setText("0"+cTakenString+" min,"+remTakenString+" sec");
            }

            if(remRemaining<10) {
                String cTakenString=String.valueOf(cRemaining);
                String remRemainingString=String.valueOf(remRemaining);
                text6.setText("0"+cTakenString+" min,"+"0"+remRemainingString+" sec");
            }
            else
            {
                String cTakenString=String.valueOf(cRemaining);
                String remRemainingString=String.valueOf(remRemaining);
                text6.setText("0"+cTakenString+" min,"+remRemainingString+" sec");
            }

            break;
        case "3":

            text2.setText(scorec);
           /* text4.setText(""+String.format("%d min,%d sec", TimeUnit.MILLISECONDS.toMinutes(timeTakenCLong),
                    TimeUnit.MILLISECONDS.toSeconds(timeTakenCLong)-
                            TimeUnit.MINUTES.toSeconds(TimeUnit.MILLISECONDS.toMinutes(timeTakenCLong))));
            text6.setText(""+String.format("%d min,%d sec", TimeUnit.MILLISECONDS.toMinutes(timeRemainingCLong),
                    TimeUnit.MILLISECONDS.toSeconds(timeRemainingCLong)-
                            TimeUnit.MINUTES.toSeconds(TimeUnit.MILLISECONDS.toMinutes(timeRemainingCLong))));*/
            if(remTaken<10) {
                String cTakenString=String.valueOf(cTaken);
                String remTakenString=String.valueOf(remTaken);
                text4.setText("0"+cTakenString+" min,"+"0"+remTakenString+" sec");
            }
            else
            {
                String cTakenString=String.valueOf(cTaken);
                String remTakenString=String.valueOf(remTaken);
                text4.setText("0"+cTakenString+" min,"+remTakenString+" sec");
            }

            if(remRemaining<10) {
                String cTakenString=String.valueOf(cRemaining);
                String remRemainingString=String.valueOf(remRemaining);
                text6.setText("0"+cTakenString+" min,"+"0"+remRemainingString+" sec");
            }
            else
            {
                String cTakenString=String.valueOf(cRemaining);
                String remRemainingString=String.valueOf(remRemaining);
                text6.setText("0"+cTakenString+" min,"+remRemainingString+" sec");
            }

            break;
        case "4":

            text2.setText(scorec);
           /* text4.setText(""+String.format("%d min,%d sec", TimeUnit.MILLISECONDS.toMinutes(timeTakenCLong),
                    TimeUnit.MILLISECONDS.toSeconds(timeTakenCLong)-
                            TimeUnit.MINUTES.toSeconds(TimeUnit.MILLISECONDS.toMinutes(timeTakenCLong))));
            text6.setText(""+String.format("%d min,%d sec", TimeUnit.MILLISECONDS.toMinutes(timeRemainingCLong),
                    TimeUnit.MILLISECONDS.toSeconds(timeRemainingCLong)-
                            TimeUnit.MINUTES.toSeconds(TimeUnit.MILLISECONDS.toMinutes(timeRemainingCLong))));*/

            // textView1.setText("Good Job");
            if(remTaken<10) {
                String cTakenString=String.valueOf(cTaken);
                String remTakenString=String.valueOf(remTaken);
                text4.setText("0"+cTakenString+" min,"+"0"+remTakenString+" sec");
            }
            else
            {
                String cTakenString=String.valueOf(cTaken);
                String remTakenString=String.valueOf(remTaken);
                text4.setText("0"+cTakenString+" min,"+remTakenString+" sec");
            }

            if(remRemaining<10) {
                String cTakenString=String.valueOf(cRemaining);
                String remRemainingString=String.valueOf(remRemaining);
                text6.setText("0"+cTakenString+" min,"+"0"+remRemainingString+" sec");
            }
            else
            {
                String cTakenString=String.valueOf(cRemaining);
                String remRemainingString=String.valueOf(remRemaining);
                text6.setText("0"+cTakenString+" min,"+remRemainingString+" sec");
            }
            break;
        case "5":

            text2.setText(scorec);
           /* text4.setText(""+String.format("%d min,%d sec", TimeUnit.MILLISECONDS.toMinutes(timeTakenCLong),
                    TimeUnit.MILLISECONDS.toSeconds(timeTakenCLong)-
                            TimeUnit.MINUTES.toSeconds(TimeUnit.MILLISECONDS.toMinutes(timeTakenCLong))));
            text6.setText(""+String.format("%d min,%d sec", TimeUnit.MILLISECONDS.toMinutes(timeRemainingCLong),
                    TimeUnit.MILLISECONDS.toSeconds(timeRemainingCLong)-
                            TimeUnit.MINUTES.toSeconds(TimeUnit.MILLISECONDS.toMinutes(timeRemainingCLong))));*/

            //textView1.setText("Very Good Job");
            if(remTaken<10) {
                String cTakenString=String.valueOf(cTaken);
                String remTakenString=String.valueOf(remTaken);
                text4.setText("0"+cTakenString+" min,"+"0"+remTakenString+" sec");
            }
            else
            {
                String cTakenString=String.valueOf(cTaken);
                String remTakenString=String.valueOf(remTaken);
                text4.setText("0"+cTakenString+" min,"+remTakenString+" sec");
            }

            if(remRemaining<10) {
                String cTakenString=String.valueOf(cRemaining);
                String remRemainingString=String.valueOf(remRemaining);
                text6.setText("0"+cTakenString+" min,"+"0"+remRemainingString+" sec");
            }
            else
            {
                String cTakenString=String.valueOf(cRemaining);
                String remRemainingString=String.valueOf(remRemaining);
                text6.setText("0"+cTakenString+" min,"+remRemainingString+" sec");
            }
            break;

    }
}

else if(scoreJava!=null) {
    switch (scoreJava) {
        case "0":
            txt2.setText(scoreJava);
            if(remTaken<10) {
                String cTakenString=String.valueOf(cTaken);
                String remTakenString=String.valueOf(remTaken);
                txt4.setText("0"+cTakenString+" min,"+"0"+remTakenString+" sec");
            }
            else
            {
                String cTakenString=String.valueOf(cTaken);
                String remTakenString=String.valueOf(remTaken);
                txt4.setText("0"+cTakenString+" min,"+remTakenString+" sec");
            }

            if(remRemaining<10) {
                String cTakenString=String.valueOf(cRemaining);
                String remRemainingString=String.valueOf(remRemaining);
                txt6.setText("0"+cTakenString+" min,"+"0"+remRemainingString+" sec");
            }
            else
            {
                String cTakenString=String.valueOf(cRemaining);
                String remRemainingString=String.valueOf(remRemaining);
                txt6.setText("0"+cTakenString+" min,"+remRemainingString+" sec");
            }

            break;
        case "1":

            txt2.setText(scoreJava);
            if(remTaken<10) {
                String cTakenString=String.valueOf(cTaken);
                String remTakenString=String.valueOf(remTaken);
                txt4.setText("0"+cTakenString+" min,"+"0"+remTakenString+" sec");
            }
            else
            {
                String cTakenString=String.valueOf(cTaken);
                String remTakenString=String.valueOf(remTaken);
                txt4.setText("0"+cTakenString+" min,"+remTakenString+" sec");
            }

            if(remRemaining<10) {
                String cTakenString=String.valueOf(cRemaining);
                String remRemainingString=String.valueOf(remRemaining);
                txt6.setText("0"+cTakenString+" min,"+"0"+remRemainingString+" sec");
            }
            else
            {
                String cTakenString=String.valueOf(cRemaining);
                String remRemainingString=String.valueOf(remRemaining);
                txt6.setText("0"+cTakenString+" min,"+remRemainingString+" sec");
            }

            break;
        case "2":

            txt2.setText(scoreJava);
            if(remTaken<10) {
                String cTakenString=String.valueOf(cTaken);
                String remTakenString=String.valueOf(remTaken);
                txt4.setText("0"+cTakenString+" min,"+"0"+remTakenString+" sec");
            }
            else
            {
                String cTakenString=String.valueOf(cTaken);
                String remTakenString=String.valueOf(remTaken);
                txt4.setText("0"+cTakenString+" min,"+remTakenString+" sec");
            }

            if(remRemaining<10) {
                String cTakenString=String.valueOf(cRemaining);
                String remRemainingString=String.valueOf(remRemaining);
                txt6.setText("0"+cTakenString+" min,"+"0"+remRemainingString+" sec");
            }
            else
            {
                String cTakenString=String.valueOf(cRemaining);
                String remRemainingString=String.valueOf(remRemaining);
                txt6.setText("0"+cTakenString+" min,"+remRemainingString+" sec");
            }

            break;
        case "3":

            txt2.setText(scoreJava);
            if(remTaken<10) {
                String cTakenString=String.valueOf(cTaken);
                String remTakenString=String.valueOf(remTaken);
                txt4.setText("0"+cTakenString+" min,"+"0"+remTakenString+" sec");
            }
            else
            {
                String cTakenString=String.valueOf(cTaken);
                String remTakenString=String.valueOf(remTaken);
                txt4.setText("0"+cTakenString+" min,"+remTakenString+" sec");
            }

            if(remRemaining<10) {
                String cTakenString=String.valueOf(cRemaining);
                String remRemainingString=String.valueOf(remRemaining);
                txt6.setText("0"+cTakenString+" min,"+"0"+remRemainingString+" sec");
            }
            else
            {
                String cTakenString=String.valueOf(cRemaining);
                String remRemainingString=String.valueOf(remRemaining);
                txt6.setText("0"+cTakenString+" min,"+remRemainingString+" sec");
            }

            break;
        case "4":
                txt2.setText(scoreJava);
            if(remTaken<10) {
                String cTakenString=String.valueOf(cTaken);
                String remTakenString=String.valueOf(remTaken);
                txt4.setText("0"+cTakenString+" min,"+"0"+remTakenString+" sec");
            }
            else
            {
                String cTakenString=String.valueOf(cTaken);
                String remTakenString=String.valueOf(remTaken);
                txt4.setText("0"+cTakenString+" min,"+remTakenString+" sec");
            }

            if(remRemaining<10) {
                String cTakenString=String.valueOf(cRemaining);
                String remRemainingString=String.valueOf(remRemaining);
                txt6.setText("0"+cTakenString+" min,"+"0"+remRemainingString+" sec");
            }
            else
            {
                String cTakenString=String.valueOf(cRemaining);
                String remRemainingString=String.valueOf(remRemaining);
                txt6.setText("0"+cTakenString+" min,"+remRemainingString+" sec");
            }

            // textView1.setText("Good Job");
            break;
        case "5":

            txt2.setText(scoreJava);
            if(remTaken<10) {
                String cTakenString=String.valueOf(cTaken);
                String remTakenString=String.valueOf(remTaken);
                txt4.setText("0"+cTakenString+" min,"+"0"+remTakenString+" sec");
            }
            else
            {
                String cTakenString=String.valueOf(cTaken);
                String remTakenString=String.valueOf(remTaken);
                txt4.setText("0"+cTakenString+" min,"+remTakenString+" sec");
            }

            if(remRemaining<10) {
                String cTakenString=String.valueOf(cRemaining);
                String remRemainingString=String.valueOf(remRemaining);
                txt6.setText("0"+cTakenString+" min,"+"0"+remRemainingString+" sec");
            }
            else
            {
                String cTakenString=String.valueOf(cRemaining);
                String remRemainingString=String.valueOf(remRemaining);
                txt6.setText("0"+cTakenString+" min,"+remRemainingString+" sec");
            }

            //textView1.setText("Very Good Job");
            break;

    }
}

        else if(scoreAndroid!=null) {
    switch (scoreAndroid) {
        case "0":
            tx2.setText(scoreAndroid);
            if(remAndroidTaken<10) {
                String cTakenString=String.valueOf(cAndroidTaken);
                String remTakenString=String.valueOf(remAndroidTaken);
                tx4.setText("0"+cTakenString+" min,"+"0"+remTakenString+" sec");
            }
            else
            {
                String cTakenString=String.valueOf(cAndroidTaken);
                String remTakenString=String.valueOf(remAndroidTaken);
                tx4.setText("0"+cTakenString+" min,"+remTakenString+" sec");
            }

            if(remAndroidRemaining<10) {
                String cTakenString=String.valueOf(cAndroidRemaining);
                String remRemainingString=String.valueOf(remAndroidRemaining);
                tx6.setText("0"+cTakenString+" min,"+"0"+remRemainingString+" sec");
            }
            else
            {
                String cTakenString=String.valueOf(cAndroidRemaining);
                String remRemainingString=String.valueOf(remAndroidRemaining);
                tx6.setText("0"+cTakenString+" min,"+remRemainingString+" sec");
            }

            break;
        case "1":

            tx2.setText(scoreAndroid);
            if(remAndroidTaken<10) {
                String cTakenString=String.valueOf(cAndroidTaken);
                String remTakenString=String.valueOf(remAndroidTaken);
                tx4.setText("0"+cTakenString+" min,"+"0"+remTakenString+" sec");
            }
            else
            {
                String cTakenString=String.valueOf(cAndroidTaken);
                String remTakenString=String.valueOf(remAndroidTaken);
                tx4.setText("0"+cTakenString+" min,"+remTakenString+" sec");
            }

            if(remAndroidRemaining<10) {
                String cTakenString=String.valueOf(cAndroidRemaining);
                String remRemainingString=String.valueOf(remAndroidRemaining);
                tx6.setText("0"+cTakenString+" min,"+"0"+remRemainingString+" sec");
            }
            else
            {
                String cTakenString=String.valueOf(cAndroidRemaining);
                String remRemainingString=String.valueOf(remAndroidRemaining);
                tx6.setText("0"+cTakenString+" min,"+remRemainingString+" sec");
            }

            break;
        case "2":

            tx2.setText(scoreAndroid);
            if(remAndroidTaken<10) {
                String cTakenString=String.valueOf(cAndroidTaken);
                String remTakenString=String.valueOf(remAndroidTaken);
                tx4.setText("0"+cTakenString+" min,"+"0"+remTakenString+" sec");
            }
            else
            {
                String cTakenString=String.valueOf(cAndroidTaken);
                String remTakenString=String.valueOf(remAndroidTaken);
                tx4.setText("0"+cTakenString+" min,"+remTakenString+" sec");
            }

            if(remAndroidRemaining<10) {
                String cTakenString=String.valueOf(cAndroidRemaining);
                String remRemainingString=String.valueOf(remAndroidRemaining);
                tx6.setText("0"+cTakenString+" min,"+"0"+remRemainingString+" sec");
            }
            else
            {
                String cTakenString=String.valueOf(cAndroidRemaining);
                String remRemainingString=String.valueOf(remAndroidRemaining);
                tx6.setText("0"+cTakenString+" min,"+remRemainingString+" sec");
            }

            break;
        case "3":
            tx2.setText(scoreAndroid);
            if(remAndroidTaken<10) {
                String cTakenString=String.valueOf(cAndroidTaken);
                String remTakenString=String.valueOf(remAndroidTaken);
                tx4.setText("0"+cTakenString+" min,"+"0"+remTakenString+" sec");
            }
            else
            {
                String cTakenString=String.valueOf(cAndroidTaken);
                String remTakenString=String.valueOf(remAndroidTaken);
                tx4.setText("0"+cTakenString+" min,"+remTakenString+" sec");
            }

            if(remAndroidRemaining<10) {
                String cTakenString=String.valueOf(cAndroidRemaining);
                String remRemainingString=String.valueOf(remAndroidRemaining);
                tx6.setText("0"+cTakenString+" min,"+"0"+remRemainingString+" sec");
            }
            else
            {
                String cTakenString=String.valueOf(cAndroidRemaining);
                String remRemainingString=String.valueOf(remAndroidRemaining);
                tx6.setText("0"+cTakenString+" min,"+remRemainingString+" sec");
            }

            break;
        case "4":
            tx2.setText(scoreAndroid);
            // textView1.setText("Good Job");
            if(remAndroidTaken<10) {
                String cTakenString=String.valueOf(cAndroidTaken);
                String remTakenString=String.valueOf(remAndroidTaken);
                tx4.setText("0"+cTakenString+" min,"+"0"+remTakenString+" sec");
            }
            else
            {
                String cTakenString=String.valueOf(cAndroidTaken);
                String remTakenString=String.valueOf(remAndroidTaken);
                tx4.setText("0"+cTakenString+" min,"+remTakenString+" sec");
            }

            if(remAndroidRemaining<10) {
                String cTakenString=String.valueOf(cAndroidRemaining);
                String remRemainingString=String.valueOf(remAndroidRemaining);
                tx6.setText("0"+cTakenString+" min,"+"0"+remRemainingString+" sec");
            }
            else
            {
                String cTakenString=String.valueOf(cAndroidRemaining);
                String remRemainingString=String.valueOf(remAndroidRemaining);
                tx6.setText("0"+cTakenString+" min,"+remRemainingString+" sec");
            }

            break;
        case "5":
            tx2.setText(scoreAndroid);
            //textView1.setText("Very Good Job");
            if(remAndroidTaken<10) {
                String cTakenString=String.valueOf(cAndroidTaken);
                String remTakenString=String.valueOf(remAndroidTaken);
                tx4.setText("0"+cTakenString+" min,"+"0"+remTakenString+" sec");
            }
            else
            {
                String cTakenString=String.valueOf(cAndroidTaken);
                String remTakenString=String.valueOf(remAndroidTaken);
                tx4.setText("0"+cTakenString+" min,"+remTakenString+" sec");
            }

            if(remAndroidRemaining<10) {
                String cTakenString=String.valueOf(cAndroidRemaining);
                String remRemainingString=String.valueOf(remAndroidRemaining);
                tx6.setText("0"+cTakenString+" min,"+"0"+remRemainingString+" sec");
            }
            else
            {
                String cTakenString=String.valueOf(cAndroidRemaining);
                String remRemainingString=String.valueOf(remAndroidRemaining);
                tx6.setText("0"+cTakenString+" min,"+remRemainingString+" sec");
            }

            break;

    }
}

        restart.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent i=new Intent(ResultActivity.this,CategoryActivity.class);
                startActivity(i);
                finish();
            }
        });
        restartj.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent i=new Intent(ResultActivity.this,CategoryActivity.class);
                startActivity(i);
                finish();
            }
        });
        restarta.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent i=new Intent(ResultActivity.this,CategoryActivity.class);
                startActivity(i);
                finish();
            }
        });
        home.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent i=new Intent(ResultActivity.this,CategoryActivity.class);
                startActivity(i);
                finish();
            }
        });
        homej.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent i=new Intent(ResultActivity.this,CategoryActivity.class);
                startActivity(i);
                finish();
            }
        });
        homea.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent i=new Intent(ResultActivity.this,CategoryActivity.class);
                startActivity(i);
                finish();
            }
        });
        close.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent i=new Intent(ResultActivity.this,CategoryActivity.class);
                startActivity(i);
                finish();
            }
        });
        closej.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent i=new Intent(ResultActivity.this,CategoryActivity.class);
                startActivity(i);
                finish();
            }
        });
        closea.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent i=new Intent(ResultActivity.this,CategoryActivity.class);
                startActivity(i);
                finish();
            }
        });
    }
    /*public static ResultActivity getActivityInstance()
    {
     return INSTANCE;

    }
    public String getData()
    {
        return this.scorec;
    }*/
    public void onBackPressed()
    {

        AlertDialog.Builder builder=new AlertDialog.Builder(ResultActivity.this);
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
}
