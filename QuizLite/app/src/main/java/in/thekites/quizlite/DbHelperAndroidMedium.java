package in.thekites.quizlite;

import android.content.ContentValues;
import android.content.Context;
import android.database.Cursor;
import android.database.sqlite.SQLiteDatabase;
import android.database.sqlite.SQLiteOpenHelper;

import java.util.ArrayList;
import java.util.List;

/**
 * Created by Ankit on 2016-10-31.
 */
public class DbHelperAndroidMedium extends SQLiteOpenHelper {
    private static final int DATABASE_VERSION=2;
    private static final String DATABASE_NAME="androidquizmedium";
    private static final String TABLE_QUEST="quest";

    private static final String KEY_ID="id";
    private static final String KEY_QUES="question";
    private static final String KEY_ANSWER="answer";
    private static final String KEY_OPTA="opta";
    private static final String KEY_OPTB="optb";
    private static final String KEY_OPTC="optc";

    private SQLiteDatabase dbase;




    public DbHelperAndroidMedium (Context context)
    {
        super(context,DATABASE_NAME,null,DATABASE_VERSION);
    }
    @Override
    public void onCreate(SQLiteDatabase db) {

        dbase=db;
        String sql="CREATE TABLE IF NOT EXISTS "+TABLE_QUEST+" ( "+
                KEY_ID+" INTEGER PRIMARY KEY AUTOINCREMENT, "+KEY_QUES+" TEXT,"+
                KEY_ANSWER+" TEXT, "+KEY_OPTA+" TEXT, "+KEY_OPTB+" TEXT, "+KEY_OPTC+" TEXT)";
        db.execSQL(sql);
        addQuestions();
    }

    public void addQuestion(Question quest)
    {
        ContentValues values=new ContentValues();
        values.put(KEY_QUES,quest.getQUESTION());
        values.put(KEY_ANSWER,quest.getANSWER());
        values.put(KEY_OPTA,quest.getOPTA());
        values.put(KEY_OPTB,quest.getOPTB());
        values.put(KEY_OPTC,quest.getOPTC());

        dbase.insert(TABLE_QUEST,null,values);

    }

    private  void addQuestions()
    {
        Question q1=new Question("1.Which driver of android is "+" not open source?","Keypad","Wifi","Audio","Wifi");
        this.addQuestion(q1);
        Question q2=new Question("2. Which among are not part of"+" native android libraries?","Webkit","Opengl","Dalvik","Dalvik");
        this.addQuestion(q2);
        Question q3=new Question("3. Which O.S is used as base"+" of Android Stack?","Linux","Windows","Java","Linux");
        this.addQuestion(q3);
        Question q4=new Question("4. Which year DVM development"+" started?","2005","2006","2007","2005");
        this.addQuestion(q4);
        Question q5=new Question("5. Which of these is not main component"+" of the APK?","Dalvikexe","Resources","Webkit","Webkit");
        this.addQuestion(q5);

    }

    public List<AndroidQuestion> getAllQuestions()
    {
        List<AndroidQuestion>quesList=new ArrayList<AndroidQuestion>();

        String selectQuery="SELECT * FROM "+TABLE_QUEST;
        dbase=this.getReadableDatabase();
        Cursor cursor=dbase.rawQuery(selectQuery,null);

        if(cursor.moveToFirst())
        {
            do{
                AndroidQuestion quest=new AndroidQuestion();
                quest.setID(cursor.getInt(0));
                quest.setQUESTION(cursor.getString(1));
                quest.setANSWER(cursor.getString(2));
                quest.setOPTA(cursor.getString(3));
                quest.setOPTB(cursor.getString(4));
                quest.setOPTC(cursor.getString(5));

                quesList.add(quest);
            }while(cursor.moveToNext());

        }
        return quesList;
    }

    public int rowCount()
    {
        int row=0;
        String selectQuery="SELECT * FROM "+TABLE_QUEST;
        SQLiteDatabase db=this.getWritableDatabase();
        Cursor cursor=db.rawQuery(selectQuery,null);
        row=cursor.getCount();
        return  row;
    }

    @Override
    public void onUpgrade(SQLiteDatabase db, int oldVersion, int newVersion) {

        db.execSQL("DROP TABLE IF EXISTS "+TABLE_QUEST);
        onCreate(db);

    }
}
