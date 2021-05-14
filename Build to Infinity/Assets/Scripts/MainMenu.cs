using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using UnityEngine.SceneManagement;
public class MainMenu : MonoBehaviour {

	public Text scoreText;
	private void Start()
	{
		scoreText.text = PlayerPrefs.GetInt ("score").ToString();
	}
	public void toGame()
	{
		SceneManager.LoadScene ("Levels");

	}
	public void toAbout()
	{

		SceneManager.LoadScene ("About");
	}

	}
