# Date: August 14th, 2025
## Device: Makerbot 3D printer
## Database ID: (tbd)


## Description:
User of makerbot 3D printer has given me it, stating that the extruder head does not reach temperature anymore. The device has been gathering dust, unplugged for years.

## Diagnostics: 
> 1. Firstly, I had pulled up documentation regarding the 3D printer from the manufacturer.
     It was here I had confirmed that most of the parts of this machine are no longer manufactured,
>    and they go for heafty prices online. If the extruder head was indeed the problem, it would not
>    be within budget.
> 2. I fired up the machine to test it out, confirmed, the extruder head was not reaching temperature.
> 3. Theory of probable cause: Insufficent power
> 4. Test the theory: I opened up the machine and found a powersupply in the very back after completely dissasembling the frame. It had a P1 power connector.
>    I had my power supply tester on hand and confirmed that two 3.3V rails were not providing enough power, and a 12V rail was at 13.6V. Board description
>    indicates that this was a power supply failure.
> 5. Confirm with user: I did some investigating into the user's setup talking to them personally, most likely cause of power supply failure was that the
>    3D printer was plugged directly into the wall in a geographical location prone to power surges/outages.
> 6. Establish preventative measures: User has acquired a newer, more modern and open-source 3D printer, I have suggested acquiring a surge protector and UPS.
> 7. Documentation: Here.
>
## Key Takeaway:
3D printers are complex devices, but unless the printer head shows direct signs of burning, swelling, or odd smells, usually shown by the insulation on the extruder and heat sink,
the problem might stem from more simple causes of improper power hygiene. 

## Further Notes:
I can easily repair this 3D printer, I have the model of the power supply logged, and will consider acquiring a higher quality or more relevant one for this board. I will firstly,
however, run further diagnostics on the board and devices to test to see if the board itself was affected by the low voltage. Gives me further experience later on in embedded systems
diagnostics.

