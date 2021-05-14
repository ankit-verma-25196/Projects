using UnityEngine;
using UnityEngine.EventSystems;
using System.Collections;
using UnityEngine.UI;
using UnityEngine.SceneManagement;
//using UnityEngine.GUIText;

public class TheStack : MonoBehaviour {

	public bool paused;
	public AudioClip tak;
	//public AudioClip fail;
	public Text scoreText;
	public Color32[] gameColors=new Color32[4];
	public Material stackMap;
	public GameObject endPanel;
	public GameObject NewHighScore;

	public Button pauseBtn;

	private AudioSource source;
	//private AudioSource source2;
	private float volLowRange=.5f;
	private float volHighRange=1.0f;
	private const float BOUNDS_SIZE = 3.5f;
	private const float STACK_MOVING_SPEED = 5.0f;
	private const float ERROR_MARGIN = 0.1f;
	private const float STACK_BOUNDS_GAIN = 0.25f;
	private const int COMBO_START_GAIN = 3;
	private GameObject[] theStack;
	private Vector2 stackBounds = new Vector2 (BOUNDS_SIZE, BOUNDS_SIZE);
	private int scoreCount=0;
	private int combo = 0;
	private int stackIndex;
	private float tileTransition=0.0f;
	private float tileSpeed=1.5f;
	private bool isMovingOnX=true;
	private bool gameOver=false;
	private float secondaryPosition;
	private Vector3 desiredPosition;
	private Vector3 lastTilePosition;
	// Use this for initialization
	void Start () {
		paused = false;
		theStack=new GameObject[transform.childCount];

		for (int i=0; i<transform.childCount; i++) {
			theStack [i] = transform.GetChild (i).gameObject;
			ColorMesh(theStack[i].GetComponent<MeshFilter>().mesh);

         }
		stackIndex = transform.childCount-1;
		PlayerPrefs.SetInt ("score", 2);
		//source2 = GetComponent<AudioSource> ();
	}
	private void createRubble(Vector3 pos,Vector3 scale)
	{
		GameObject go = GameObject.CreatePrimitive (PrimitiveType.Cube);
		go.transform.localPosition = pos;
		go.transform.localScale = scale;
		go.AddComponent<Rigidbody> ();

		go.GetComponent<MeshRenderer> ().material = stackMap;
		ColorMesh(go.GetComponent<MeshFilter>().mesh);

	}
	void Awake()
	{
		source = GetComponent<AudioSource> ();

	}
	public void pause()
	{
		paused = !paused;
		if (paused) {
			Time.timeScale = 0;
		}
		else if (!paused) {
			Time.timeScale = 1;
		}
	}
	
	// Update is called once per frame
	IEnumerator high()
	{
		if (PlayerPrefs.GetInt ("score") < scoreCount) {
			//pause ();
			NewHighScore.SetActive (true);
	
			yield return new WaitForSeconds (2.5f);
			NewHighScore.SetActive (false);
		}
	}
	void Update () {


			
		if (Input.GetMouseButtonDown (0)) {
			
			/*if (EventSystem.current.currentSelectedGameObject) {
				
				Time.timeScale = 0;
			} else if (!EventSystem.current.currentSelectedGameObject) {
				Debug.Log ("Hello");*/
				//tileSpeed = 1.5f;
				
				if (placeTile ()) {
					float vol = Random.Range (volLowRange, volHighRange);
					source.PlayOneShot (tak, vol);
					spawnTile ();
					scoreCount++;
					scoreText.text = scoreCount.ToString ();
					high ();
				
				} else {
				
					endGame ();
					//float vol = Random.Range (volLowRange, volHighRange);
					//source2.PlayOneShot (fail, vol);
				}
			//}
		}
			

			moveTile ();
			//Move the stack
			transform.position = Vector3.Lerp (transform.position, desiredPosition, STACK_MOVING_SPEED * Time.deltaTime);

		

				
	}
	private void moveTile()
	{
		if (gameOver)
			return;
		tileTransition += Time.deltaTime * tileSpeed;
		if(isMovingOnX)
			theStack [stackIndex].transform.localPosition = new Vector3 (Mathf.Sin (tileTransition)*BOUNDS_SIZE, scoreCount, secondaryPosition);
		else
			theStack [stackIndex].transform.localPosition = new Vector3 (secondaryPosition, scoreCount, Mathf.Sin (tileTransition)*BOUNDS_SIZE);


	}
	private void spawnTile()
	{
		lastTilePosition = theStack [stackIndex].transform.localPosition;
		stackIndex--;
		if (stackIndex < 0)
			stackIndex = transform.childCount - 1;

		desiredPosition = (Vector3.down) * scoreCount;

		theStack [stackIndex].transform.localPosition = new Vector3 (0, scoreCount, 0);
		theStack [stackIndex].transform.localScale = new Vector3 (stackBounds.x, 1, stackBounds.y);

		ColorMesh(theStack[stackIndex].GetComponent<MeshFilter>().mesh);
	}
	private bool placeTile()
	{
		Transform t = theStack [stackIndex].transform;

		if (isMovingOnX) {
			float deltaX = lastTilePosition.x - t.position.x;
			if (Mathf.Abs (deltaX) > ERROR_MARGIN) {
				//CUT the Tile
				combo = 0;
				stackBounds.x -= Mathf.Abs (deltaX);
				if (stackBounds.x <= 0)
					return false;

				float middle = lastTilePosition.x + t.localPosition.x / 2;
				t.localScale = new Vector3 (stackBounds.x, 1, stackBounds.y);
				createRubble(new Vector3((t.position.x>0)
				                         ?t.position.x+(t.localScale.x/2)
				                         :t.position.x-(t.localScale.x/2),t.position.y,t.position.z),
				             new Vector3(Mathf.Abs (deltaX),1,t.localScale.z)
				             );

				t.localPosition = new Vector3 (middle - (lastTilePosition.x / 2), scoreCount, lastTilePosition.z);
			
			}
			else{
				if(combo>COMBO_START_GAIN)
				{
					stackBounds.x+=STACK_BOUNDS_GAIN;
					if(stackBounds.x>BOUNDS_SIZE)
						stackBounds.x=BOUNDS_SIZE;
					float middle = lastTilePosition.x + t.localPosition.x / 2;
					t.localScale = new Vector3 (stackBounds.x, 1, stackBounds.y);

					t.localPosition = new Vector3 (middle - (lastTilePosition.x / 2), scoreCount, lastTilePosition.z);

				}
				combo++;
				t.localPosition =new Vector3(lastTilePosition.x,scoreCount,lastTilePosition.z);
			}
		} else {
			float deltaZ = lastTilePosition.z - t.position.z;
			if (Mathf.Abs (deltaZ) > ERROR_MARGIN) {
				//CUT the Tile
				combo = 0;
				stackBounds.y -= Mathf.Abs (deltaZ);
				if (stackBounds.y <= 0)
					return false;
				
				float middle = lastTilePosition.z + t.localPosition.z / 2;
				t.localScale = new Vector3 (stackBounds.x, 1, stackBounds.y);
				createRubble(new Vector3(t.position.x,t.position.y,(t.position.z>0)
				                         ?t.position.z+(t.localScale.z/2)
				                         :t.position.z-(t.localScale.z/2)),
				             new Vector3(t.localScale.x,1,Mathf.Abs (deltaZ))
				             );

				t.localPosition = new Vector3 (lastTilePosition.x, scoreCount, middle - (lastTilePosition.z / 2));

			}
			else{
				if(combo>COMBO_START_GAIN)
				{
					if(stackBounds.y>BOUNDS_SIZE)
						stackBounds.y=BOUNDS_SIZE;
					stackBounds.y+=STACK_BOUNDS_GAIN;
					
					float middle = lastTilePosition.z + t.localPosition.z / 2;
					t.localScale = new Vector3 (stackBounds.x, 1, stackBounds.y);
					t.localPosition = new Vector3 (lastTilePosition.x, scoreCount, middle - (lastTilePosition.z / 2));
					

				}
				combo++;
				t.localPosition =new Vector3(lastTilePosition.x,scoreCount,lastTilePosition.z);

			}
		}
		secondaryPosition = (isMovingOnX)
			? t.localPosition.x
				: t.localPosition.z;
		isMovingOnX = !isMovingOnX;

		return true;
	}

	private void ColorMesh(Mesh mesh)
	{
		Vector3[] vertices = mesh.vertices;
		Color32[] colors = new Color32[vertices.Length];
		float f = Mathf.Sin (scoreCount * 0.25f);

		for (int i=0; i<vertices.Length; i++)
 			colors [i] = Lerp4 (gameColors [0], gameColors [1], gameColors [2], gameColors [3],f);
		mesh.colors32 = colors;

	}
	private Color32 Lerp4(Color32 a,Color32 b,Color32 c,Color32 d,float t)
	{
	if (t < 0.33f)
			return Color.Lerp (a, b, t / 0.33f);
		else if (t < 0.66f)
			return Color.Lerp (b, c, (t - 0.33f) / 0.33f);
		else
			return Color.Lerp (c,d,(t-0.66f)/0.66f);
	}
	/*IEnumerator showMessage(string message ,float delay)
	{
		guiText.text =  message;
		UnityEngine.GUIText.enabled = true;
		yield return new WaitForSeconds (delay);
		UnityEngine.GUIText.enabled = false;
	}*/

	private void endGame()
	{
		if (PlayerPrefs.GetInt ("score") < scoreCount) {
			PlayerPrefs.SetInt ("score", scoreCount);
			//StartCoroutine (showMessage ("New HighScore", 5));
			//var Noti="NEW HighScore";
			//EditorWindow.ShowNotification(GUIContent Noti);
		}
			gameOver = true;

		endPanel.SetActive (true);

		theStack [stackIndex].AddComponent<Rigidbody> ();
	}

	public void OnButtonClick()
	{
		SceneManager.LoadScene ("Game");
	}
	public void OnButtonClick2()
	{
		SceneManager.LoadScene ("Menu");
	}
	public void OnButtonClick3()
	{
		SceneManager.LoadScene ("Levels");
	}

}
