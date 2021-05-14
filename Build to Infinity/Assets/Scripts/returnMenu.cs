using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class returnMenu : MonoBehaviour {

	public void toMenu()
	{

		SceneManager.LoadScene ("Menu");
	}

	public void toSettings()
	{

		//SceneManager.LoadScene ("About");
	}

}
