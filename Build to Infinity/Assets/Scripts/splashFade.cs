using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using UnityEngine.SceneManagement;

public class splashFade : MonoBehaviour {

	public Image splashImage;
	public Image splashImage2;
	public Text presents;
	// Use this for initialization
	IEnumerator Start () {

		splashImage.canvasRenderer.SetAlpha (0.0f);
		splashImage2.canvasRenderer.SetAlpha (0.0f);
		presents.canvasRenderer.SetAlpha (0.0f);
		FadeIn ();
		yield return new WaitForSeconds (2.5f);
		FadeOut ();
		yield return new WaitForSeconds (2.5f);
		SceneManager.LoadScene ("Menu");
	}

	void FadeIn()
	{
		splashImage.CrossFadeAlpha (1.0f, 1.5f, false);
		splashImage2.CrossFadeAlpha (1.0f, 1.5f, false);
		presents.CrossFadeAlpha (1.0f, 1.5f, false);
	}
	void FadeOut()
	{
		splashImage.CrossFadeAlpha (0.0f, 2.5f, false);
		splashImage2.CrossFadeAlpha (0.0f, 2.5f, false);
		presents.CrossFadeAlpha (0.0f, 2.5f, false);
	}

}
