import struct
import math

# These below are the Byte indexes, written in order

RaceOn = 0

TimeStamp = 4

MaxRPM = 8
IdleRPM = 12
CurrentRPM = 16

AccelerationX = 20
AccelerationY = 24
AccelerationZ = 28

VelocityX = 32
VelocityY = 36
VelocityZ = 40

AngularVelocityX = 44
AngularVelocityY = 48
AngularVelocityZ = 52

Yaw = 56
Pitch = 60
Roll = 64

NormalizedSuspensionTravelFL = 68
NormalizedSuspensionTravelFR = 72
NormalizedSuspensionTravelRL = 76
NormalizedSuspensionTravelRR = 80

TireSlipRatioFL = 84
TireSlipRatioFR = 88
TireSlipRatioRL = 92
TireSlipRatioRR = 96

WheelRotationSpeedFL = 100
WheelRotationSpeedFR = 104
WheelRotationSpeedRL = 108
WheelRotationSpeedRR = 112

WheelOnRumbleStripFL = 116
WheelOnRumbleStripFR = 120
WheelOnRumbleStripRL = 124
WheelOnRumbleStripRR = 128

WheelInPuddleDepthFL = 132
WheelInPuddleDepthFR = 136
WheelInPuddleDepthRL = 140
WheelInPuddleDepthRR = 144

SurfaceRumbleFrontLeft = 148
SurfaceRumbleFrontRight = 152
SurfaceRumbleRearLeft = 156
SurfaceRumbleRearRight = 160

TireSlipAngleFL = 164
TireSlipAngleFR = 168
TireSlipAngleRL = 172
TireSlipAngleRR = 176

TireCombinedSlipFL = 180
TireCombinedSlipFR = 184
TireCombinedSlipRL = 188
TireCombinedSlipRR = 192

SuspensionTravelMetersFL = 196
SuspensionTravelMetersFR = 200
SuspensionTravelMetersRL = 204
SuspensionTravelMetersRR = 208

CarClass = 216
CarPerformanceIndex = 220

DrivetrainType = 224
NumberOfCylinders = 228

CarType = 232
ObjectHit = 236

# Byte unknown
# Byte unknown
# Byte unknown
# Byte unknown
# Byte unknown
# Byte unknown

Ordinal = 240

PositionX = 244
PositionY = 248
PositionZ = 252

Speed = 256
Power = 260
Torque = 264

TireTempFL = 268
TireTempFR = 272
TireTempRL = 276
TireTempRR = 280

Boost = 284

Fuel = 288

DistanceTraveled = 292

BestLap = 296
LastLap = 300
CurrentLap = 304
CurrentRaceTime = 308
LapNumber = 312

RacePosition = 314

Throttle = 315
Brake = 316
Clutch = 317
HandBrake = 318
Gear = 319

Steer = 320

NormalizedDrivingLine = 321

NormalizedAIBrakeDifference = 322


# Variables for timer function
t1 = 0
t2 = 0


def get_race_on(DataBytes):
    variants = {
        0: 'OFF',
        1: 'ON',
    }
    try:
        race_on = struct.unpack('<H', DataBytes[RaceOn : RaceOn + 2])     
        return variants.get(race_on[0])
    except:
        return("Error calling: get_race_on")


def get_time_stamp(DataBytes):
    try:
        time_stamp = struct.unpack('<l', DataBytes[TimeStamp : TimeStamp + 4])     
        return time_stamp[0]
    except:
        return("Error calling: get_time_stamp")


def get_max_rpm(DataBytes):
    try:
        max_rpm = struct.unpack('<f', DataBytes[MaxRPM : MaxRPM + 4])     
        return int(max_rpm[0])
    except:
        return("Error calling: get_max_rpm")


def get_idle_rpm(DataBytes):
    try:
        IDLE_rpm = struct.unpack('<f', DataBytes[IdleRPM : IdleRPM + 4])     
        return int(IDLE_rpm[0])
    except:
        return("Error calling: get_idle_rpm")


def get_rpm(DataBytes):
    try:
        turatia = struct.unpack('<f', DataBytes[CurrentRPM : CurrentRPM + 4])     
        return int(turatia[0])
    except:
        return("Error calling: get_rpm")


def get_AccelX(DataBytes):
    try:
        accelX = struct.unpack('<f', DataBytes[AccelerationX : AccelerationX + 4])     
        return accelX[0] / 9.81
    except:
        return("Error calling: get_AccelX")  


def get_AccelY(DataBytes):
    try:
        accelY = struct.unpack('<f', DataBytes[AccelerationY : AccelerationY + 4])     
        return accelY[0] / 9.81
    except:
        return("Error calling: get_AccelY")    


def get_AccelZ(DataBytes):
    try:
        accelZ = struct.unpack('<f', DataBytes[AccelerationZ : AccelerationZ + 4])     
        return accelZ[0] / 9.81
    except:
        return("Error calling: get_AccelZ")


def get_Rez_Accel(DataBytes):
    ax = round(get_AccelX(DataBytes))
    ay = round(get_AccelY(DataBytes))
    az = round(get_AccelZ(DataBytes))
    return math.sqrt(int(ax)**2 + int(ay)**2 + int(az)**2)


def get_VelocityX(DataBytes):
    try:
        VelX = struct.unpack('<f', DataBytes[VelocityX : VelocityX + 4])     
        return VelX[0] * 3.6
    except:
        return("Error calling: get_VelocityX")


def get_VelocityY(DataBytes):
    try:
        VelY = struct.unpack('<f', DataBytes[VelocityY : VelocityY + 4])     
        return VelY[0] * 3.6
    except:
        return("Error calling: get_VelocityY")


def get_VelocityZ(DataBytes):
    try:
        VelZ = struct.unpack('<f', DataBytes[VelocityZ : VelocityZ + 4])     
        return VelZ[0] * 3.6
    except:
        return("Error calling: get_VelocityZ")


def get_angular_VelocityX(DataBytes):
    try:
        AngVelX = struct.unpack('<f', DataBytes[AngularVelocityX : AngularVelocityX + 4])     
        return AngVelX[0]
    except:
        return("Error calling: get_angular_VelocityX")


def get_angular_VelocityY(DataBytes):
    try:
        AngVelY = struct.unpack('<f', DataBytes[AngularVelocityY : AngularVelocityY + 4])     
        return AngVelY[0]
    except:
        return("Error calling: get_angular_VelocityY")


def get_angular_VelocityZ(DataBytes):
    try:
        AngVelZ = struct.unpack('<f', DataBytes[AngularVelocityZ : AngularVelocityZ + 4])     
        return AngVelZ[0]
    except:
        return("Error calling: get_angular_VelocityZ")


def get_Yaw(DataBytes):
    try:
        yaw = struct.unpack('<f', DataBytes[Yaw : Yaw + 4])     
        return yaw[0] * 100
    except:
        return("Error calling: get_Yaw")


def get_Pitch(DataBytes):
    try:
        pitch = struct.unpack('<f', DataBytes[Pitch : Pitch + 4])     
        return pitch[0] * 100
    except:
        return("Error calling: get_Pitch")


def get_Roll(DataBytes):
    try:
        roll = struct.unpack('<f', DataBytes[Roll : Roll + 4])     
        return roll[0] * 100
    except:
        return("Error calling: get_Roll")


def get_normalized_suspension_travel_FL(DataBytes):
    try:
        nstfl = struct.unpack('<f', DataBytes[NormalizedSuspensionTravelFL : NormalizedSuspensionTravelFL + 4])
        return nstfl[0] * 100
    except:
        return("Error calling: get_normalized_suspension_travel_FL")


def get_normalized_suspension_travel_FR(DataBytes):
    try:
        nstfr = struct.unpack('<f', DataBytes[NormalizedSuspensionTravelFR : NormalizedSuspensionTravelFR + 4])
        return nstfr[0] * 100
    except:
        return("Error calling: get_normalized_suspension_travel_FR")


def get_normalized_suspension_travel_RL(DataBytes):
    try:
        nstrl = struct.unpack('<f', DataBytes[NormalizedSuspensionTravelRL : NormalizedSuspensionTravelRL + 4])
        return nstrl[0] * 100
    except:
        return("Error calling: get_normalized_suspension_travel_RL")


def get_normalized_suspension_travel_RR(DataBytes):
    try:
        nstrr = struct.unpack('<f', DataBytes[NormalizedSuspensionTravelRR : NormalizedSuspensionTravelRR + 4])
        return nstrr[0] * 100
    except:
        return("Error calling: get_normalized_suspension_travel_RR")


def get_tire_slip_ratio_FL(DataBytes):
    try:
        tsrfl = struct.unpack('<f', DataBytes[TireSlipRatioFL : TireSlipRatioFL + 4])
        return tsrfl[0] * 100
    except:
        return("Error calling: get_tire_slip_ratio_FL")


def get_tire_slip_ratio_FR(DataBytes):
    try:
        tsrfr = struct.unpack('<f', DataBytes[TireSlipRatioFR : TireSlipRatioFR + 4])
        return tsrfr[0] * 100
    except:
        return("Error calling: get_tire_slip_ratio_FR")


def get_tire_slip_ratio_RL(DataBytes):
    try:
        tsrrl = struct.unpack('<f', DataBytes[TireSlipRatioRL : TireSlipRatioRL + 4])
        return tsrrl[0] * 100
    except:
        return("Error calling: get_tire_slip_ratio_RL")


def get_tire_slip_ratio_RR(DataBytes):
    try:
        tsrrr = struct.unpack('<f', DataBytes[TireSlipRatioRR : TireSlipRatioRR + 4])
        return tsrrr[0] * 100
    except:
        return("Error calling: get_tire_slip_ratio_RR")


def get_wheel_rot_Speed_FL(DataBytes):
    try:
        rsfl = struct.unpack('<f', DataBytes[WheelRotationSpeedFL : WheelRotationSpeedFL + 4])
        return rsfl[0]
    except:
        return("Error calling: get_wheel_rot_Speed_FL")


def get_wheel_rot_Speed_FR(DataBytes):
    try:
        rsfr = struct.unpack('<f', DataBytes[WheelRotationSpeedFR : WheelRotationSpeedFR + 4])
        return rsfr[0]
    except:
        return("Error calling: get_wheel_rot_Speed_FR")


def get_wheel_rot_Speed_RL(DataBytes):
    try:
        rsrl = struct.unpack('<f', DataBytes[WheelRotationSpeedRL : WheelRotationSpeedRL + 4])
        return rsrl[0]
    except:
        return("Error calling: get_wheel_rot_Speed_RL")


def get_wheel_rot_Speed_RR(DataBytes):
    try:
        rsrr = struct.unpack('<f', DataBytes[WheelRotationSpeedRR : WheelRotationSpeedRR + 4])
        return rsrr[0]
    except:
        return("Error calling: get_wheel_rot_Speed_RR")


def get_slip_angle_FL(DataBytes):
    try:
        tsfl = struct.unpack('<f', DataBytes[TireSlipAngleFL : TireSlipAngleFL + 4])
        return tsfl[0]
    except:
        return("Error calling: get_slip_angle_FL")


def get_slip_angle_FR(DataBytes):
    try:
        tsfr = struct.unpack('<f', DataBytes[TireSlipAngleFR : TireSlipAngleFR + 4])
        return tsfr[0]
    except:
        return("Error calling: get_slip_angle_FR")


def get_slip_angle_RL(DataBytes):
    try:
        tsrl = struct.unpack('<f', DataBytes[TireSlipAngleRL : TireSlipAngleRL + 4])
        return tsrl[0]
    except:
        return("Error calling: get_slip_angle_RL")


def get_slip_angle_RR(DataBytes):
    try:
        tsrr = struct.unpack('<f', DataBytes[TireSlipAngleRR : TireSlipAngleRR + 4])
        return tsrr[0]
    except:
        return("Error calling: get_slip_angle_RR")


def get_tire_combined_slip_FL(DataBytes):
    try:
        tcsfl = struct.unpack('<f', DataBytes[TireCombinedSlipFL : TireCombinedSlipFL + 4])
        return tcsfl[0]
    except:
        return("Error calling: get_tire_combined_slip_FL")


def get_tire_combined_slip_FR(DataBytes):
    try:
        tcsfr = struct.unpack('<f', DataBytes[TireCombinedSlipFR : TireCombinedSlipFR + 4])
        return tcsfr[0]
    except:
        return("Error calling: get_tire_combined_slip_FR")


def get_tire_combined_slip_RL(DataBytes):
    try:
        tcsrl = struct.unpack('<f', DataBytes[TireCombinedSlipRL : TireCombinedSlipRL + 4])
        return tcsrl[0]
    except:
        return("Error calling: get_tire_combined_slip_RL")


def get_tire_combined_slip_RR(DataBytes):
    try:
        tcsrr = struct.unpack('<f', DataBytes[TireCombinedSlipRR : TireCombinedSlipRR + 4])
        return tcsrr[0]
    except:
        return("Error calling: get_tire_combined_slip_RR")


def get_suspension_travel_FL(DataBytes):
    try:
        stfl = struct.unpack('<f', DataBytes[SuspensionTravelMetersFL : SuspensionTravelMetersFL + 4])
        return stfl[0]
    except:
        return("Error calling: get_suspension_travel_FL")


def get_suspension_travel_FR(DataBytes):
    try:
        stfr = struct.unpack('<f', DataBytes[SuspensionTravelMetersFR : SuspensionTravelMetersFR + 4])
        return stfr[0]
    except:
        return("Error calling: get_suspension_travel_FR")


def get_suspension_travel_RL(DataBytes):
    try:
        strl = struct.unpack('<f', DataBytes[SuspensionTravelMetersRL : SuspensionTravelMetersRL + 4])
        return strl[0]
    except:
        return("Error calling: get_suspension_travel_RL")


def get_suspension_travel_RR(DataBytes):
    try:
        strr = struct.unpack('<f', DataBytes[SuspensionTravelMetersRR : SuspensionTravelMetersRR + 4])
        return strr[0]
    except:
        return("Error calling: get_suspension_travel_RR")


def get_corresp_car_class(CCVal):
    CarClassCases = {
        0: "D",
        1: "C",
        2: "B",
        3: "A",
        4: "S1",
        5: "S2",
        6: "X",
    }
    return CarClassCases.get(CCVal, 'Not_found')


def get_car_class(DataBytes):
    try:
        Car_class = struct.unpack('<i', DataBytes[CarClass : CarClass + 4])     
        return get_corresp_car_class(Car_class[0])
    except:
        return("Error calling: get_car_class")


def get_performance_index(DataBytes):
    try:
        PerfIndex = struct.unpack('<i', DataBytes[CarPerformanceIndex : CarPerformanceIndex + 4])     
        return PerfIndex[0]
    except:
        return("Error calling: get_performance_index")


def get_corresp_drivetrain(DtVal):
    DrivetrainCases = {
        0: "FWD",
        1: "RWD",
        2: "AWD",
    }
    return DrivetrainCases.get(DtVal, 'Not_found')


def get_drivetrain_type(DataBytes):
    try:
        DType = struct.unpack('<i', DataBytes[DrivetrainType : DrivetrainType + 4])     
        return get_corresp_drivetrain(DType[0])
    except:
        return("Error calling: get_drivetrain_type")


def get_num_of_cyl(DataBytes):
    try:
        Num_cyl = struct.unpack('<i', DataBytes[NumberOfCylinders : NumberOfCylinders + 4])     
        return Num_cyl[0]
    except:
        return("Error calling: get_num_of_cyl")


def get_CoordX(DataBytes):
    try:
        CoordX = struct.unpack('<f', DataBytes[PositionX : PositionX + 4])     
        return CoordX[0]
    except:
        return("Error calling: get_CoordX")
    

def get_CoordY(DataBytes):
    try:
        CoordY = struct.unpack('<f', DataBytes[PositionY : PositionY + 4])     
        return CoordY[0]
    except:
        return("Error calling: get_CoordY")


def get_CoordZ(DataBytes):
    try:
        CoordZ = struct.unpack('<f', DataBytes[PositionZ : PositionZ + 4])     
        return CoordZ[0]
    except:
        return("Error calling: get_CoordZ")


def get_Speed(DataBytes):
    try:
        speed = struct.unpack('<f', DataBytes[Speed : Speed + 4])     
        return speed[0] * 3.6
    except:
        return("Error calling: get_Speed")


def get_Power(DataBytes):
    try:
        power = struct.unpack('<f', DataBytes[Power : Power + 4])     
        return power[0] * 0.00134102
    except:
        return("Error calling: get_Power")


def get_Torque(DataBytes):
    try:
        Tq = struct.unpack('<f', DataBytes[Torque : Torque + 4])     
        return Tq[0]
    except:
        return("Error calling: get_Torque")


def get_Tire_temp_FL(DataBytes):
    try:
        tire_temp_FL = struct.unpack('<f', DataBytes[TireTempFL : TireTempFL + 4])     
        return (tire_temp_FL[0] - 32) * (5/9)
    except:
        return("Error calling: get_Tire_temp_FL")


def get_Tire_temp_FR(DataBytes):
    try:
        tire_temp_FR = struct.unpack('<f', DataBytes[TireTempFR : TireTempFR + 4])     
        return (tire_temp_FR[0] - 32) * (5/9)
    except:
        return("Error calling: get_Tire_temp_FR")


def get_Tire_temp_RL(DataBytes):
    try:
        tire_temp_RL = struct.unpack('<f', DataBytes[TireTempRL : TireTempRL + 4])     
        return (tire_temp_RL[0] - 32) * (5/9)
    except:
        return("Error calling: get_Tire_temp_RL")


def get_Tire_temp_RR(DataBytes):
    try:
        tire_temp_RR = struct.unpack('<f', DataBytes[TireTempRR : TireTempRR + 4])     
        return (tire_temp_RR[0] - 32) * (5/9)
    except:
        return("Error calling: get_Tire_temp_RR")


def get_Boost(DataBytes):
    try:
        boost = struct.unpack('<f', DataBytes[Boost : Boost + 4])     
        return round(boost[0] * 0.0689475729, 3)
    except:
        return("Error calling: get_Boost")


def get_Fuel(DataBytes):
    try:
        fuel = struct.unpack('<h', DataBytes[Fuel : Fuel + 4])     
        return fuel[0]
    except:
        return("Error calling: get_Fuel")


def get_distance_traveled(DataBytes):
    try:
        Dist = struct.unpack('<h', DataBytes[DistanceTraveled : DistanceTraveled + 4])     
        return Dist[0]
    except:
        return("Error calling: get_distance_traveled")


def get_best_lap(DataBytes):
    try:
        BestLap = struct.unpack('<h', DataBytes[BestLap : BestLap + 4])     
        return BestLap[0]
    except:
        return("Error calling: get_best_lap")


def get_last_lap(DataBytes):
    try:
        LastLap = struct.unpack('<h', DataBytes[LastLap : LastLap + 4])     
        return LastLap[0]
    except:
        return("Error calling: get_last_lap")


def get_current_lap(DataBytes):
    try:
        CurrentLap_ = struct.unpack('<h', DataBytes[CurrentLap : CurrentLap + 4])     
        return CurrentLap_[0]
    except:
        return("Error calling: get_current_lap")


def get_current_race_time(DataBytes):
    try:
        RaceTime = struct.unpack('<h', DataBytes[CurrentRaceTime : CurrentRaceTime + 4])     
        return RaceTime[0]
    except:
        return("Error calling: get_current_race_time")


def get_lap_number(DataBytes):
    try:
        LapNum = struct.unpack('<h', DataBytes[LapNumber : LapNumber + 2])     
        return LapNum[0]
    except:
        return("Error calling: get_lap_number")


def get_race_position(DataBytes):
    try:
        RacePos = DataBytes[RacePosition]
        return RacePos
    except:
        return("Error calling: get_race_position")


def get_Throttle_status(DataBytes):
    try:
        Throttle_status = DataBytes[Throttle]
        return Throttle_status * 100 / 255
    except:
        return("Error calling: get_Throttle_status")


def get_Brake_status(DataBytes):
    try:
        Brake_status = DataBytes[Brake]
        return Brake_status * 100 / 255
    except:
        return("Error calling: get_Brake_status")


def get_Clutch_status(DataBytes):
    try:
        Clutch_status = DataBytes[Clutch]
        return Clutch_status * 100 / 255
    except:
        return("Error calling: get_Clutch_status")


def get_HandBrake_status(DataBytes):
    try:
        HandBrake_stat = DataBytes[HandBrake]
        HandBrake_stat = HandBrake_stat * 100 / 255
        if HandBrake_stat > 0:
            return 'Active'
        else:
            return 'NotActive'
    except:
        return("Error calling: get_HandBrake_status")


def get_Gear(DataBytes):
    try:
        gear = DataBytes[Gear]
        return gear
    except:
        return("Error calling: get_Gear")


def get_Steering_input(DataBytes):
    try:
        Steering_input = DataBytes[Steer]
        return Steering_input * 100 / 127
    except:
        return("Error calling: get_Steering_input")


def get_norm_driving_line(DataBytes):
    try:
        driving_line = DataBytes[NormalizedDrivingLine]
        return driving_line
    except:
        return("Error calling: get_norm_driving_line")


def get_norm_AI_brake_diff(DataBytes):
    try:
        brake_diff = DataBytes[NormalizedAIBrakeDifference]
        return brake_diff
    except:
        return("Error calling: get_norm_AI_brake_diff")


def timer(DataBytes, FinalSpeed):
    if(int(round(get_Speed(DataBytes))) <= 1 and get_HandBrake_status(DataBytes) == 'Active'):
        global t1
        t1 = int(get_time_stamp(DataBytes))
        print(f"T1 has been assigned to: {t1}")
    if(FinalSpeed == int(round(get_Speed(DataBytes)))):
        global t2
        t2 = int(get_time_stamp(DataBytes))
        print(f"T2 has been assigned to: {t2}")
        return (t2 - t1) / 1000