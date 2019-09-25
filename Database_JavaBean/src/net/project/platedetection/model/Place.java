package net.project.platedetection.model;

public class Place {

	protected int id;
	
	protected String car_plate;
	protected String place_name;
	protected boolean isEmpty;
	
	public Place() {
		super();
	}

	public Place(int id) {
		super();
		this.id = id;
	}

	public Place(int id, String car_plate, String place_name, boolean isEmpty) {
		super();
		this.id = id;
		this.car_plate = car_plate;
		this.place_name = place_name;
		this.isEmpty = isEmpty;
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

	public String getPlace_name() {
		return place_name;
	}

	public void setPlace_name(String place_name) {
		this.place_name = place_name;
	}

	public boolean isEmpty() {
		return isEmpty;
	}

	public void setEmpty(boolean isEmpty) {
		this.isEmpty = isEmpty;
	}
}
