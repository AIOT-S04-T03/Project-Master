package net.project.platedetection.model;

public class Car {

	protected int id;
	
	protected String car_plate;
	protected String car_place;
	
	protected String enter_time;
	
	public Car() {
		super();
	}

	public Car(int id) {
		super();
		this.id = id;
	}

	public Car(int id, String car_plate, String car_place, String enter_time) {
		super();
		this.id = id;
		this.car_plate = car_plate;
		this.car_place = car_place;
		this.enter_time = enter_time;
	}

	public int getId() {
		return id;
	}

	public void setId(int id) {
		this.id = id;
	}

	public String getCar_plate() {
		return car_plate;
	}

	public void setCar_plate(String car_plate) {
		this.car_plate = car_plate;
	}

	public String getCar_place() {
		return car_place;
	}

	public void setCar_place(String car_place) {
		this.car_place = car_place;
	}

	public String getEnter_time() {
		return enter_time;
	}

	public void setEnter_time(String enter_time) {
		this.enter_time = enter_time;
	}
}
