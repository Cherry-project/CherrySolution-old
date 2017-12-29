package cherry.chatterbot.web;

import cherry.robothandlers.service.LaunchPresentation;
import cherry.robothandlers.service.LaunchPrimitive;
import cherry.robothandlers.web.SetupController;

import java.io.IOException;
import java.util.Random;

import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class ChatterbotController {
	@CrossOrigin
	@RequestMapping("/chatterbot")
	public static void Chatterbot() throws IOException, InterruptedException {

		System.out.println("\nRobot utilisé : " + SetupController.robotList.get(0).getName());

		// LaunchPresentation.robotsUsed = new HashSet<String>();
		// Get the first robot connected
		try {
			LaunchPresentation.robotsUsed.add(SetupController.robotList.get(0));
		} catch (Exception e) {
			System.out.println("\n No robot available");
		}

		// Dialog
		// User
		// System.out.println("\nUtilisateur : " + msg);
		//
		// String response = new String();
		// //Get response from bot
		// response = Chatterbot.sendToChatterbot(msg);
		//
		// // Bot
		// System.out.println("\nBot : " + response);

		// Make the robot speak
		// LaunchPrimitive.startSpeakPrimitive(response);
		String[] behave = new String[9];
		behave[0] = "left_arm_up_behave";
		behave[1] = "show_right_behave";
		behave[2] = "open_arms_behave";
		behave[3] = "show_left_up_behave";
		behave[4] = "question_behave";
		behave[5] = "point_arm_right_behave";
		behave[6] = "point_arms_behave";
		behave[7] = "show_left_behave";
		behave[8] = "swap_behave";
		Random r = new Random();
		int Low = 0;
		int High = 9;
		int Result = r.nextInt(High - Low) + Low;
		LaunchPrimitive.startBehaviorPrimitive(behave[Result]);

	}

	@CrossOrigin
	@RequestMapping("/chatterbotIdle")
	public static void ChatterbotIdle() throws IOException, InterruptedException {

		System.out.println("\nRobot utilisé : " + SetupController.robotList.get(0).getName());

		// LaunchPresentation.robotsUsed = new HashSet<String>();
		// Get the first robot connected
		try {
			LaunchPresentation.robotsUsed.add(SetupController.robotList.get(0));
		} catch (Exception e) {
			System.out.println("\n No robot available");
		}

		// Dialog
		// User
		// System.out.println("\nUtilisateur : " + msg);
		//
		// String response = new String();
		// //Get response from bot
		// response = Chatterbot.sendToChatterbot(msg);
		//
		// // Bot
		// System.out.println("\nBot : " + response);

		// Make the robot speak
		// LaunchPrimitive.startSpeakPrimitive(response);
		LaunchPrimitive.startBehaviorPrimitive("torso_idle_motion");
	}

	@CrossOrigin
	@RequestMapping("/chatterbotRest")
	public static void ChatterbotRest() throws IOException {

		System.out.println("\nRobot utilisé : " + SetupController.robotList.get(0).getName());

		// LaunchPresentation.robotsUsed = new HashSet<String>();
		// Get the first robot connected
		try {
			LaunchPresentation.robotsUsed.add(SetupController.robotList.get(0));
		} catch (Exception e) {
			System.out.println("\n No robot available");
		}

		// Dialog
		// User
		// System.out.println("\nUtilisateur : " + msg);
		//
		// String response = new String();
		// //Get response from bot
		// response = Chatterbot.sendToChatterbot(msg);
		//
		// // Bot
		// System.out.println("\nBot : " + response);

		// Make the robot speak
		// LaunchPrimitive.stopPrimitive("chatterbotV0");
		LaunchPrimitive.startBehaviorPrimitive("rest_open_behave");

	}

	@CrossOrigin
	@RequestMapping("/behaveHello")
	public static void BehaveHello() throws IOException {

		System.out.println("\nRobot utilisé : " + SetupController.robotList.get(0).getName());

		// LaunchPresentation.robotsUsed = new HashSet<String>();
		// Get the first robot connected
		try {
			LaunchPresentation.robotsUsed.add(SetupController.robotList.get(0));
		} catch (Exception e) {
			System.out.println("\n No robot available");
		}

		// Dialog
		// User
		// System.out.println("\nUtilisateur : " + msg);
		//
		// String response = new String();
		// //Get response from bot
		// response = Chatterbot.sendToChatterbot(msg);
		//
		// // Bot
		// System.out.println("\nBot : " + response);

		// Make the robot speak
		// LaunchPrimitive.stopPrimitive("chatterbotV0");
		LaunchPrimitive.startBehaviorPrimitive("behave_hello");

	}

	@CrossOrigin
	@RequestMapping("/chatterbotSorry")
	public static void ChatterbotSorry() throws IOException {

		System.out.println("\nRobot utilisé : " + SetupController.robotList.get(0).getName());

		// LaunchPresentation.robotsUsed = new HashSet<String>();
		// Get the first robot connected
		try {
			LaunchPresentation.robotsUsed.add(SetupController.robotList.get(0));
		} catch (Exception e) {
			System.out.println("\n No robot available");
		}

		// Dialog
		// User
		// System.out.println("\nUtilisateur : " + msg);
		//
		// String response = new String();
		// //Get response from bot
		// response = Chatterbot.sendToChatterbot(msg);
		//
		// // Bot
		// System.out.println("\nBot : " + response);

		// Make the robot speak
		// LaunchPrimitive.stopPrimitive("chatterbotV0");
		LaunchPrimitive.startBehaviorPrimitive("behave_nope");

	}

	@CrossOrigin
	@RequestMapping("/chatterbotStop")
	public static void ChatterbotStop() throws IOException {

		System.out.println("\nRobot utilisé : " + SetupController.robotList.get(0).getName());

		// LaunchPresentation.robotsUsed = new HashSet<String>();
		// Get the first robot connected
		try {
			LaunchPresentation.robotsUsed.add(SetupController.robotList.get(0));
		} catch (Exception e) {
			System.out.println("\n No robot available");
		}

		// Dialog
		// User
		// System.out.println("\nUtilisateur : " + msg);
		//
		// String response = new String();
		// //Get response from bot
		// response = Chatterbot.sendToChatterbot(msg);
		//
		// // Bot
		// System.out.println("\nBot : " + response);

		// Make the robot speak
		LaunchPrimitive.stopPrimitive("chatterbotV0");

	}
}
