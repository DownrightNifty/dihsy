# 😮 Wait, I thought the EU mandated that?{data-group=eu-sideloading}
The [Digital Markets Act](https://digital-markets-act.ec.europa.eu/index_en) is a recent EU antitrust law with the stated goal of making digital markets "fairer and more contestable". [Article 6(4)](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=uriserv%3AOJ.L_.2022.265.01.0001.01.ENG&toc=OJ%3AL%3A2022%3A265%3ATOC#art_6) reads as follows:

> The gatekeeper shall allow and technically enable the installation and effective use of third-party software applications or software application stores using, or interoperating with, its operating system and allow those software applications or software application stores to be accessed by means other than the relevant core platform services of that gatekeeper. The gatekeeper shall, where applicable, not prevent the downloaded third-party software applications or software application stores from prompting end users to decide whether they want to set that downloaded software application or software application store as their default. The gatekeeper shall technically enable end users who decide to set that downloaded software application or software application store as their default to carry out that change easily.
> 
> The gatekeeper shall not be prevented from taking, to the extent that they are strictly necessary and proportionate, measures to ensure that third-party software applications or software application stores do not endanger the integrity of the hardware or operating system provided by the gatekeeper, provided that such measures are duly justified by the gatekeeper.
> 
> Furthermore, the gatekeeper shall not be prevented from applying, to the extent that they are strictly necessary and proportionate, measures and settings other than default settings, enabling end users to effectively protect security in relation to third-party software applications or software application stores, provided that such measures and settings other than default settings are duly justified by the gatekeeper.

Since Apple was designated as a gatekeeper under the DMA, and its mobile operating systems iOS and iPadOS were designated as core platform services, Apple is obligated to comply with the above rules. As a consequence, support for third party app stores in the EU was introduced with iOS 17.4 in March 2024.

**Unfortunately, the terms of Apple's compliance leave much to be desired, and "sideloading", as per the [conventional definition](#what-would-it-mean-for-ios-to-have-sideloading), is still not available on iOS:**

- All apps and app updates distributed outside the App Store still must be manually reviewed by employees at Apple, approved, and "notarized", else iOS will reject their installation. The criteria Apple uses to determine whether or not to approve the app is a [subset of the App Store guidelines](#macos-vs.-ios-notarization-process) (with an emphasis on privacy and security).
- Furthermore, on top of the $100/yr Apple Developer subscription required to submit apps for notarization, Apple also collects a significant ["Core Technology Fee"](https://developer.apple.com/support/core-technology-fee) from developers distributing outside the App Store, easily totaling to a much higher percentage cut than the App Store's 30%, and possibly creating a net loss or even bankrupting the app developer, making alternative distribution an unattractive option in most cases. (Note that fee waivers are available for fully non-commercial apps.)

The DMA also does not enable certain types of apps which are already available through [unofficial sideloading methods](#how-do-i-sideload-unofficially-on-ios):

- Apps that require JIT for performance, such as advanced emulators and virtual machine apps, with the exception of approved web browser apps (of which there are currently none) [^1]
	- [UTM](https://getutm.app/) is an example of such an app.
- Apps that use private APIs or OS frameworks in an "unintended" manner (as per [notarization guideline 2.5.1](https://developer.apple.com/app-store/review/guidelines/#software-requirements))
	- Riley Testut's clipboard manager app, "Clip", was [initially rejected](https://www.theverge.com/24100979/altstore-europe-app-marketplace-price-games#:~:text=For%20example%2C%20after%20I%20had%20tested%20Clip%2C%20Testut%20had%20to%20tweak%20the%20app%E2%80%99s) under this policy.

Due to the aforementioned caveats, I will henceforth be referring to these apps as "alternative apps" rather than "sideloaded apps".

Apple believes that its notarization guidelines for alternative apps do not violate the DMA due to the exception provided in Article 6(4), which allows gatekeepers to take measures to ensure that alternative apps don't "endanger the integrity of the hardware or operating system", if said measures are "strictly necessary and proportionate".

Not everyone agrees with Apple's interpretation of the DMA, however. Epic Games has described Apple's changes as ["malicious compliance"](https://www.theverge.com/2024/1/25/24050696/epic-games-tim-sweeney-apple-app-store-response). The Free Software Foundation Europe has released [multiple statements](https://fsfe.org/news/2024/news-20240627-01.en.html) arguing that Apple's notarization process is not in compliance with the DMA, since (1) third party apps on iOS don't possess the capability to compromise the integrity of the OS and (2) on macOS, Apple's other computing platform, users can choose to install apps that aren't notarized by Apple (provided they accept the risks involved), yet macOS still manages to provide a relatively secure computing environment. It should also be noted that while users are highly encouraged to only run notarized apps on macOS, the notarization requirements for macOS are [much less stringent](#macos-vs.-ios-notarization-process) and don't impede legitimate (non-malicious) developers in any meaningful way, unlike the iOS requirements.

As of the time of writing, the European Commission is still in the process of enforcing the DMA and interpreting compliance obligations. A [non-compliance investigation](https://digital-markets-act.ec.europa.eu/commission-sends-preliminary-findings-apple-and-opens-additional-non-compliance-investigation-2024-06-24_en) against Apple was opened in June 2024 regarding "the contractual requirements imposed on alternative app developers" such as the Core Technology Fee, and another investigation regarding "the checks and reviews put in place by Apple to validate apps and alternative app stores to be sideloaded" may be opened soon.

To ensure compliance, Apple should follow in the footsteps of other digital gatekeepers and provide a means for advanced users who accept the risks to sideload freely. For examples of how Apple could do this without impacting non-technical users, see [here](#do-other-devices-support-sideloading).

# 🧑‍💻 Can hobbyists take advantage of the EU's DMA today?{data-group=eu-sideloading}
While the DMA does not (as of the time of writing) enable true sideloading, it does theoretically enable opportunities for hobbyist developers to create apps that would have otherwise been rejected. It may also allow hobbyists with no intention of distributing to create personal apps for their own devices, provided they are willing to polish their apps to the extent that they meet Apple's notarization requirements. **Remember, Apple will be reviewing the app under the impression that you are attempting to release it publicly to iOS users around the world, so the requirements are designed with that in mind.**

With that being said:

- Apple has waived the Core Technology Fee for non-commercial apps (though not for app stores [^10]) that make no profit whatsoever, so the only fee you would pay is the $100 annual Apple Developer fee, which is required in order to submit apps for notarization.
- Apple has waived the ["minimal functionality"](https://developer.apple.com/app-store/review/guidelines/#minimum-functionality) portion of the App Store guidelines for alternative apps, which would otherwise forbid apps that aren't "particularly useful, unique, or app-like".
- **Once an app is notarized, the signature does not appear to expire, and that specific build of the app can be installed and used indefinitely on any iOS device in the EU.** You would however need to maintain your Apple Developer subscription and ensure ongoing compliance with the notarization guidelines in order to issue updates for your app.

In general, it seems as though Apple may approve hobbyist apps even if they have no clear purpose for a general audience and are only intended to be used by the developer. The limits of what Apple is willing to approve for alternative distribution have yet to be tested. Unfortunately, due to [time-based expiry of all "development" certificates](#how-do-i-sideload-unofficially-on-ios) (including paid ones), there is currently no better way to develop personal apps just for yourself, as the only (official) alternative is paying the $100 Apple Developer Program fee every year into the foreseeable future just to keep your app from expiring (even if you aren't actively updating it). It's truly a shame that Apple has created a unique situation where hobbyist developers have no better option than to pester Apple employees with pointless manual reviews just to create apps for their own personal use, which won't ever be installed on other user's devices.

<div class="alert-div">
<h2>⚠️</h2>
<p>If you're planning on publishing apps to the App Store in the future, please note that it's unclear if it's possible to switch back to the (arguably better) non-EU terms after you've already agreed to the EU terms.</p>
</div>

**You don't have to be located in the EU to submit apps for alternative distribution inside the EU.** If you want to start experimenting with alternative apps right now despite the current limitations: AltStore PAL is an officially approved third party app store available for free, allowing the installation of notarized apps from any source. You may [review their documentation here](https://faq.altstore.io/developers/distribute-with-altstore-pal). You'll need an Apple Developer subscription, and you'll need to accept the alternative EU terms.

# 🌎 Can users outside the EU access alternative apps?{data-group=eu-sideloading}
As a developer, you don't have to be in the EU to officially [submit apps for alternative distribution](#can-hobbyists-take-advantage-of-the-eus-dma-today) inside the EU.

However, in order to actually install those apps, you need to be in the EU (or at least, your device needs to believe that you are). Apple utilizes hardware sensors to determine the user's geographical location in order to check eligibility for alternative apps and marketplaces as required in the EU, in addition to requiring an Apple ID registered in the EU.

It has been demonstrated to be possible to spoof some of these checks and access EU-exclusive features such as alternative apps outside the EU on iPhones and iPads. You may read my blog post about it [here](https://downrightnifty.me/blog/2025/02/27/eu-features-outside.html). (There are no guarantees that Apple won't make it more difficult to spoof these checks in the future, so you shouldn't rely on this.)

Once a device detects that it has left the EU, **alternative apps that have already been installed will continue to work**, but they will no longer receive updates after a 30-day grace period until the device moves back to the EU.

Something else that should be noted is that users from around the world can benefit from the competition that alternative app stores bring to Apple's store in general. In fact, this has already happened; Apple's [unexpected reversal](https://www.theverge.com/2024/4/5/24122341/apple-app-store-game-emulators-super-apps) of its long-standing policy against game console emulators was most likely a result of the Digital Markets Act, as it removes one of the primary incentives users would have otherwise had for installing Riley Testut's AltStore and his popular "Delta" emulator.

# 📱 What is "sideloading"?
Sideloading is simply the act of installing apps on your computing device that haven't been explicitly reviewed and approved by the company who made the device (or the operating system running on it). Traditionally this has just been called "installing software", because it used to be the standard method before the advent of centralized app stores.

It's unclear exactly when the term (as per the above definition) was first introduced into the general discourse. But according to Google data, it was most likely around 2009 at the earliest:

![[Google Trends](https://trends.google.com/trends/explore?date=all&q=sideloading&hl=en-US) worldwide interest in "sideloading" from 2004-present](/assets/sideloading_google_trends.png){.img1}

(Not coincidentally, Apple launched the iPhone in 2007.)

It's quite unfortunate that a term with a negative connotation was coined to describe an inherently neutral activity. If I was being conspiratorial, I'd say it was all part of an elaborate profit-seeking plot by Apple to create [FUD](https://en.wikipedia.org/wiki/Fear,_uncertainty,_and_doubt) surrounding the topic. I'd tell you that "sideloading is the new [jaywalking](https://www.vox.com/2015/1/15/7551873/jaywalking-history)".

But the truth is probably more nuanced than that. Malware used to be much more prevalent (and damaging) than it is today. It's getting harder and harder for attackers to convince people to execute malicious payloads on their devices, and the App Store most likely has something to do with that. Attackers have adapted to their new environment, and are largely migrating to other techniques that aren't so easily mitigated by software locks, such as phishing and cold call scamming. That being said, our computing devices are more secure than ever from the average user's perspective.

There's no denying that the model has begun to shift from users downloading or purchasing software directly from developers, to users downloading software from an "app store" middleman. Users delegate trust to the app store to vet the software they download to ensure it works properly, isn't malicious, and isn't accessing their data without their consent. For the average user, this creates a safer environment within which they can perform their computing tasks.

The App Store model clearly has real benefits for users. It would be dishonest to claim that protecting the end user's privacy and security is Apple's only motivation for pushing this model so heavily, though. There's of course enormous incentive created by the enormous profit generated through forcing everyone to use a centralized store. Apple's Services division, which includes the App Store, is their second largest, and has remained that way since Q3 2017. In Q4 2024, Apple made 26% of their revenue from Services. The Services division has been consistently creeping upwards over time, taking away from hardware's share year after year. [^11]

We should keep in mind that this didn't happen overnight. When the iPhone was released in June 2007, it didn't have an app store, and there was no ([official](https://en.wikipedia.org/wiki/IOS_jailbreaking#JailbreakMe_and_AppSnapp)) method to install new apps. Steve Jobs described the new device "merely" as a "widescreen iPod with touch controls, a revolutionary mobile phone, and a breakthrough Internet communicator" during his unforgettable 2007 WWDC presentation. The (technically arbitrary) software limitations imposed on Apple's new [OSX-powered](https://web.archive.org/web/20220925123655/https://www.wired.com/2007/05/steve-jobs-ipho/) portable-computer-but-not-advertised-as-such did not stand in the way of its success. People were so blown away by the iPhone, that any software shortcomings could easily be excused. The iPhone SDK was released in March 2008, alongside the announcement of the App Store, and it was confirmed that the App Store would be the exclusive method for distributing apps on the platform.

It's been 17 years since the release of the iPhone, and needless to say, smartphones and other mobile computing devices have changed the world. Smartphones are no longer a "nice to have", but rather an essential item we carry with us at all times, wherever we go. We [experience anxiety](https://www.theguardian.com/lifeandstyle/2017/aug/28/does-phone-separation-anxiety-really-exist) when we realize we forgot to bring our smartphone with us.

Third party app support on iPhone, competition from Android, and [talented hackers](https://en.wikipedia.org/wiki/IOS_jailbreaking) allowed developers to begin pushing the limits of what these "phones" could do. Apple may not have realized it at the time, but it didn't just invent the modern smartphone in 2007; it invented the modern computer. iPhone OS became iOS, then iPadOS. Today, the iPad Pro is advertised as [all but a computer](https://9to5mac.com/2017/11/16/ipad-pro-whats-a-computer-ad/)! The latest iPads even use the same processors as the latest Macs.

The iPhone paved the way for the app store model and other modern computer security features which are now considered baseline, such as full device encryption and verified/secure boot. With each new iOS security feature rolling out, Apple challenged the rest of the industry to improve their own security and privacy protections. All mainstream operating systems, including Windows, macOS, Chrome OS, and Android now implement an [app sandbox](https://en.wikipedia.org/wiki/Sandbox_(computer_security)) in some way (to varying degrees of success), something the iPhone did first.

If the entire industry is moving towards Apple's approach, then we should probably start thinking about what that means for the future of personal computing. To my knowledge, we've never seen a (conventional) "computer" that isn't user-programmable enter the mainstream market. We are now, though, seeing non-conventional computers which are many times more powerful than yesterday's conventional computers on paper, but are not user-programmable. We're becoming more tolerant of artificial limitations imposed by the operating systems we're forced to run on these devices, because we're told that it's the only way we can remain secure.

I think that, for the average user, these limitations are perfectly acceptable, and indeed preferable. But at the same time, I don't think we should leave powerusers and developers in the dust as we craft this new world of secure computing. Apple has made some brilliant, ultraportable, and remarkably powerful computing devices, but the OS that runs on them is preventing users from realizing their true potential, and it's kind of sad. Implementing advanced features such as sideloading in a way that prevents social engineering attacks convincing non-technical users to enable them is non-trivial, but [definitely possible](#case-study-chromeos), and absolutely vital if we are to avoid redefining the modern "computer" as something entirely different.

# 💙 What are benefits of sideloading?
Non-exhaustive list of sideloading use cases and benefits:

- Allows the end user to [write apps for their own device](https://www.bennettnotes.com/notes/why-does-apple-restrict-hobby-development/)
	- In other words: it would enable the use of iOS devices as [general-purpose computers](https://en.wikipedia.org/wiki/Von_Neumann_architecture)
- Allows for perfectly legitimate apps that cannot be uploaded to the App Store due to its strict guidelines, creating a more fair, more free, and more open market for apps
	- Examples include:
		- Apps that require [JIT compilation](https://en.wikipedia.org/wiki/Just-in-time_compilation) to function, such as [Dolphin](https://dolphinios.oatmealdome.me/), a Wii emulator that runs beautifully on iOS using JIT
		- Apps that require JIT compilation for performance, such as [UTM](https://getutm.app/), which brings virtual machines to iOS
		- Alternative web browser engines such as Firefox (Gecko) and Chrome (Blink), which would bring competition to the space, benefiting all users
		- Alternative clients for popular services like YouTube
			- I wasn't able to find an example for iOS, but [NewPipe](https://newpipe.net/) is my preferred YouTube client on Android, and [Grayjay](https://grayjay.app/) is a promising new Android-exclusive app that combines different streaming services together
			- Despite being perfectly legal in most countries, these can't be uploaded to the App Store due to [guideline 5.2.2](https://developer.apple.com/app-store/review/guidelines/#intellectual-property)
		- Apps that use OS APIs in an "unintended" manner, such as [Clip](https://rileytestut.com/blog/2020/06/17/introducing-clip/)
		- Apps that execute code dynamically, such as [performant terminal emulators](https://ish.app/blog/ish-jit-and-eu)
	- These classes of apps used to be entirely excluded from the App Store until Apple suddenly reversed course, most likely in response to legislation, antitrust investigations, or competition from third party app stores:
		- [Game console emulators](https://www.theverge.com/2024/4/5/24122341/apple-app-store-game-emulators-super-apps), most likely to remove a primary incentive users would have otherwise had for installing Riley Testut's AltStore and his popular "Delta" emulator.
		- Cloud streaming services, most likely due to an [impending antitrust lawsuit](https://www.theverge.com/2024/3/21/24107633/apple-streaming-super-apps-doj-lawsuit).
	- Keep in mind, I could probably list even more examples if sideloading were officially supported and these apps didn't [require workarounds](#how-do-i-sideload-unofficially-on-ios) such as jailbreaking to use! It's currently difficult to justify developing iOS apps that won't be accepted into the App Store, because very few users are going to be able to actually use them.
- Allows [free and open source software (FOSS)](https://en.wikipedia.org/wiki/Free_software) to exist on iOS
	- Currently, FOSS is completely blocked by all iOS devices at the OS level! I personally believe in the value of FOSS, and I try to use as much of it as possible, but regardless of your feelings on it, it's difficult to argue that it should be completely blocked on one of the most popular computing platforms. I believe it should be given a fair chance to compete with other development models.
	- Note that open source software is not the same as FOSS. Open source software is allowed on iOS, but FOSS is not. To quality as FOSS, a software product must provide all four essential freedoms to the end user. Since end users cannot freely make changes to their own copy of any iOS app, *even if the developers want to allow this*, all iOS apps automatically violate [freedom #1 of the official Free Software Definition](https://www.gnu.org/philosophy/free-sw.en.html#four-freedoms), and as such they are not FOSS.
	- In the EU, [notarization guideline 4.3(a)](https://developer.apple.com/app-store/review/guidelines/#spam) may prevent you from using the Digital Markets Act to maintain your own private fork of an open-source app.
	- The "free" in FOSS refers to freedom, not price. FOSS can cost money. To learn more about FOSS, see [here](https://www.fsf.org/about/what-is-free-software).
- Provides users with a much higher degree of control over the computing devices that they legally and rightfully own
- Brings more flexibility to developers, and lower costs to users, through competition in third party payment processing services and app stores, and alternatives to the 30% App Store cut (+ $100/yr Apple Developer subscription)
	- Apps that rely primarily on revenue from subscriptions or in-app purchases are [especially affected](https://www.theverge.com/2019/3/16/18268811/spotify-apple-european-commission-antitrust-statement-war-of-words) by Apple's 30% cut.
	- This isn't to say that 30% is a bad deal in all cases! The App Store offers a great service to most developers, but it shouldn't be the only option.
- Repurposes older devices that no longer receive software updates and can no longer download apps from the App Store
- Circumvents any and all [censorship by Apple](https://en.wikipedia.org/wiki/Censorship_by_Apple)

# 🔒 Is sideloading safe?
Sideloading is generally safe if:

- You wrote the apps that you're sideloading yourself, or
- You carefully vet the sources of apps that you sideload, and your operating system provides some level of protection against malicious apps
	- Android and iOS enforce a strict sandbox on all apps, which ensures that apps can only access sensitive data with explicit user consent. macOS is moving towards enforcing a sandbox on apps from all sources as well, but it isn't there quite yet, so sideloading is still fairly risky. Windows 10+ has a built-in antivirus, but that doesn't protect you against unknown threats. Windows 10+ also has [opt-in app sandbox](https://learn.microsoft.com/en-us/windows/msix/msix-container), and Windows 11 [improves the sandbox further](https://learn.microsoft.com/en-us/windows/win32/secauthz/app-isolation-overview), but in practice sandboxing is rarely used. Be extra careful when sideloading on Windows.

In fact, some of the most secure systems in the world, arguably more secure than iOS, [support sideloading](#do-other-devices-support-sideloading).

Even among those who sideload, most prefer to offload these trust decisions to a third party app store. This means you only have to make a relatively high-stakes trust decision for each app store you download, which only happens once or twice in most cases. On Android, most sideloaded apps are obtained through [F-Droid](https://en.wikipedia.org/wiki/F-Droid), a trusted third party app store that only serves open source apps built using their own (also open source) infrastructure. On Windows, most sideloaded games are obtained through [Steam](https://en.wikipedia.org/wiki/Steam_(service)), a trusted third party app store that vets each game before making it available.

Ideally, third party app stores work with the underlying OS and provide the user with sufficient information about each app's author, what it does, and what sensitive data it may request access to, if any. For example, F-Droid provides a list of any Android permissions that an app may request on the app details page of every app in the store. F-Droid further provides a list of ["anti-features"](https://f-droid.org/docs/Anti-Features/) for each app, warning users of potentially undesirable behavior such as advertising or exchanging data with proprietary network services. AltStore, an alternative app store for iOS, provides information about permissions that each app may request as well. Personally, I trust F-Droid more than the Play Store or App Store, and most of my favorite apps on my Android phone come from there.

![Permission details on AltStore and F-Droid app listing pages](/assets/altstore_and_f-droid_permissions.png){.img2}

iOS and Android follow a [principle of least privilege](https://en.wikipedia.org/wiki/Principle_of_least_privilege) approach for third party apps (and usually for system apps and background processes as well). They both enforce a strict sandbox on all third party apps, regardless of where the apps were obtained from. An Android app [does not have access to any sensitive data or resources by default](https://source.android.com/docs/security/overview/app-security#the-android-permission-model-accessing-protected-apis). iOS works similarly. Users must explicitly grant access to any sensitive data or resources. As such, you can be fairly confident that, even if you accidentally installed a malicious app, it isn't able to access any sensitive data that you didn't explicitly provide it. iOS and Android apps also aren't allowed to interfere with the operating system itself, so you can safely and easily uninstall a malicious app without worrying about any lingering effects afterwards. Somewhat ironically, despite iOS refusing to allow sideloading, it's actually among the safest operating systems to sideload on.

Sideloading may not be safe for users who are not technically literate or are generally gullible, because they may be tricked into installing a malicious app and then granting said app permission to access sensitive data or resources. (Note that browsing the web carries similar risks, so all users of computing devices would ideally receive some baseline internet safety training.)

This is often touted as a reason why iOS should not support sideloading at all, but I wholeheartedly disagree. Even if sideloading isn't made generally available to all users, it can still be made available to technically-inclined users only. This isn't a trivial task, and requires a bit of thought to implement correctly, but it's very much possible and has [already been done before](#case-study-chromeos).

# 🤔 What would it mean for iOS to "have" sideloading?
For the purposes of this website, an operating system sideloading supports sideloading if it provides some officially-supported method allowing technically-inclined end users to (permanently) install [^13] native apps [^7] without any involvement of the device manufacturer, distributor, or their partners.

An operating system does not need to endorse, recommend, or make it easy to sideload in order for it to support sideloading as an option. Operating systems that only allow advanced users to sideload through scare prompts, hidden "development" modes, or any other methods still count. Operating systems that require a one-time payment (within reason) to unlock sideloading, or which require you to accept some basic terms (within reason) before you enable sideloading would also count. Operating systems employing any combination of the described techniques, or any other techniques, to discourage sideloading for the average user, or to prevent social engineering attacks convincing users to enable sideloading, still count.

For example, [we consider Chrome OS](#case-study-chromeos) to support sideloading.

Apple would not have to make sweeping changes to iOS in order to qualify; in fact, a minor policy change would be more than sufficient. For example, all it would take to qualify is for Apple to remove the unnecessary expiry dates from development certificates (which can only be used on the creator's own devices, and cannot be used for distribution). They currently expire after 7 days for free accounts, or 1 year for paid accounts.

There are several [community-supported unofficial sideloading methods](#how-do-i-sideload-unofficially-on-ios) for iOS, but those aren't guaranteed to continue working through iOS security updates, they aren't authorized by Apple and may break Apple's end user license agreement, they have significant downsides, and they don't qualify for reasons as per the first paragraph above.

# 💻 Do other devices support sideloading?
All mainstream operating systems for computing devices, besides iOS/iPadOS, support sideloading in some capacity.

| OS         | Can sideload? | Scare screen(s)? | Dev mode only? | Must accept terms? | One-time fee? |
| ---------- | ------------- | ---------------- | -------------- | ------------------ | ------------- |
| Windows    | Yes           | No               | No             | No                 | No            |
| macOS      | Yes           | Yes              | No             | No                 | No            |
| ChromeOS   | Yes           | Yes              | Yes            | Yes [^8]           | No            |
| GNU/Linux  | Yes           | No               | No             | No                 | No            |
| Android    | Yes           | Yes              | No             | No                 | No            |
| iOS/iPadOS | No            |                  |                |                    |               |

These operating systems are regarded by security experts as being extremely secure, and yet still support sideloading:

- ChromeOS
- [GrapheneOS](https://en.wikipedia.org/wiki/GrapheneOS), a security and privacy enhanced fork of Android

## Case study: ChromeOS
ChromeOS is probably the most secure mainstream consumer operating system in the world. It implements a cryptographically verified boot chain which ensures that neither the OS nor any of its components has been tampered with, mandatory full device encryption, and strict sandboxing for all third party code with no exceptions, among many other [advanced defense-in-depth security features](https://www.chromium.org/chromium-os/developer-library/reference/security/security-whitepaper/). All third party native code inside Android apps is isolated using virtualization, and on top of that, the standard Android app sandbox applies.

By default, apps can only be installed through the Google Play Store. To enable sideloading, you need to follow a complex series of steps, agree to some basic terms and conditions, factory reset your device, and enable ["developer mode"](https://www.chromium.org/chromium-os/developer-library/guides/device/developer-mode/). In addition, every time you reboot the device after enabling developer mode, you'll be reminded by the boot screen that your security is reduced and you will need to confirm that this is acceptable before the OS loads.

![ChromeOS developer mode boot warning (via [Reddit](https://www.reddit.com/r/linux4noobs/comments/1e39v78/did_somebody_install_linux_on_an_lenovo/))](/assets/chromeos_dev_mode.png){.img3}

Google created this process to ensure that it's completely infeasible for an attacker to trick someone into enabling developer mode and compromising theirself, while at the same time enabling advanced users to make full use of the hardware they purchased.

I honestly believe that, for better or for worse, this "opt-in developer mode for advanced users only" is the only sustainable approach going forward. All computers are becoming easier to use and more secure than ever before, not just iOS devices, and I think that's a good thing overall, but I also think that there should always be an "escape hatch" for advanced users (and as of the time of writing, there always is, except on iOS).

## macOS vs. iOS notarization process
Apple uses the term "notarization" to describe the approval process for apps submitted to third party app stores on iOS, which is confusing because it's they use the same term to describe a very different process on macOS.

On macOS, notarization is an automated review process that performs malware checks and basic security checks on any submitted software, in addition to requiring a verified identity as part of the Apple Developer program. Apple does not impose any guidelines, besides requiring that they are not malicious, on macOS apps submitted for notarization.

On iOS, notarization is a manual review process conducted similarly to the App Store review process. An Apple employee must manually review each app for violations of the iOS [notarization guidelines](https://developer.apple.com/help/app-store-connect/distributing-apps-in-the-european-union/submit-for-notarization/), which are a subset of the App Store guidelines, before it can be distributed on so-called "alternative" app stores. The iOS notarization guidelines include [unnecessary rules that impede legitimate apps](#what-are-benefits-of-sideloading).

Another important difference between macOS and iOS notarization is that **users can choose to run software that hasn't been notarized on macOS, if they accept the risks involved**. Of course, Apple highly recommends that users only run software that has been notarized by Apple, and macOS blocks the installation of software that isn't notarized by default. But an option, buried deep within the Privacy & Security settings, is provided, allowing advanced users to run the software of their choice.

![The seven step process for opening a non-notarized app on macOS](/assets/macOS_unsigned_app_open_flow.jpg){.img4}

# 🇪🇺 Which countries are legislating "sideloading"?

<div class="alert-div">
<h2>ℹ️</h2>
<p>The following information is provided for informational purposes only. Inclusion in the chart below is not equivalent to an endorsement of the specified bills or regulations. We're aiming to stay non-political here.</p>
</div>

Legislation regarding "sideloading" or alternative app stores is currently being developed, considered, or implemented in quite a few countries. TPAS refers to "third party app stores".

| Effective as of | Country/region | Legislation/ruling                                                                                                                        | Allows TPAS?                   | Allows sideloading? | Status      |
| :-------------- | -------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------ | ------------------- | ----------- |
| 11/1/2022       | 🇪🇺 European Union | [Digital Markets Act](https://digital-markets-act.ec.europa.eu/index_en)                                                                  | Yes                            | No, as of now [^2]  | Implemented |
| 6/12/2024 [^9]  | 🇯🇵 Japan          | [Act on Promotion of Competition for Specified Smartphone Software](https://www.jftc.go.jp/en/pressreleases/yearly-2024/June/240612.html) | Yes                            | ? [^3]              | Passed |
| 5/8/2025 [^12]  | 🇧🇷 Brazil         | [Mercado Libre v. Apple](https://sei.cade.gov.br/sei/modulos/pesquisa/md_pesq_documento_consulta_externa.php?HJ7F4wnIPj2Y8B7Bj80h1lskjh7ohC8yMfhLoDBLddbbVtapRDlsIRSGO8EfHGTjlAvVixwsF8RWAxY7K1lOCwlw9mGBV9xj89bT7n1aVU7T0oE2YGB0rHOHC39OrFWc) | Yes | ? | Passed |
| 10/7/2024       | 🇺🇸 United States  | [Epic Games v. Google](https://www.theregister.com/2024/10/07/google_android_play_store_epic/)                                            | Yes, on Android for 3 yrs [^5] | ? [^6]              | 🔴 Stalled [^14]      |
| 5/24/2024       | 🇬🇧 United Kingdom | [Digital Markets, Competition and Consumers Act](https://www.gov.uk/guidance/how-the-uks-digital-markets-competition-regime-works)        | ?                              | ?                   | Passed      |
|                 | 🇦🇺 Australia      | [Amendment to Competition and Consumer Act 2010](https://treasury.gov.au/consultation/c2024-547447)                                       | ?                              | ?                   | Proposed    |
|                 | 🇺🇸 United States  | [Open App Markets Act](https://www.congress.gov/bill/117th-congress/senate-bill/2710/text?r=23&s=1), among others                         | Yes                            | ? [^4]              | Introduced    |

For technical information about the region-locked regulatory compliance features currently implemented in iOS, see the Apple Wiki article on Apple's [Eligibility system](https://theapplewiki.com/wiki/Eligibility#Domains).

# 🔓 How do I sideload unofficially on iOS?

<div class="alert-div">
<h2>⚠️</h2>
<p>You shouldn't rely on any of these methods to keep working indefinitely as Apple continually releases security updates for iOS. The following section reflects the information available as of the time of writing and may not reflect the latest information. Use these unofficial methods at your own risk, and be aware that you might be breaking Apple's EULA.</p>
</div>

## AltStore
[AltStore](https://altstore.io/) abuses Xcode's signing service, which is intended for developers to test their apps in a limited capacity before uploading them to the App Store.

Apple provides development certificates lasting 7 days for free accounts, or 1 year for paid accounts ($100/yr, or ~$8.33/mo billed annually). Apps signed this way can only be installed on the developer's registered devices and can't be directly distributed to other users. iOS refuses to launch apps with expired certificates.

AltStore connects to a server running on your computer and automatically requests the re-signing of sideloaded applications every so often, ideally preventing them from ever expiring.

Pros:

- Can be used for free (in a limited capacity)
- Does not require a jailbreak, and can be used on recent iOS devices and versions

Cons:

- Apps signed with free certificates are subject to limitations and can't access all capabilities
- Doesn't always work reliably due to iOS background execution restrictions
- Requires an ongoing Internet connection and a home server setup
- Fundamentally reliant on Apple's signing service to work

## Jailbreaking
Jailbreaking involves exploiting accidentally-introduced security vulnerabilities in iOS to gain more control over your device. Typically, jailbreaks enable sideloading, in addition to system-level tweaks and modifications.

Pros:

- Usually provides total or near-total control over your device
- Enables unrestricted sideloading

Cons:

- Generally not supported on the latest iOS devices and versions, because it relies on Apple making big mistakes and these are usually quickly fixed with updates
- Requires avoiding OS updates, opening you up to patched vulnerabilities, reducing your security, and preventing you from taking advantage of new features

You can check if your device can be jailbroken [here](https://ios.cfw.guide/). (Hint: probably not.)

# ℹ️ Who made this website and why?
Hi, I'm [Matt](https://downrightnifty.me/). I currently use a Google Pixel (Android) phone, an iPad, and a MacBook Pro. I'll probably switch to iPhone if the answer to the question this site poses ever becomes "yes".

As part of a university project, I recently developed an iOS app that keeps track of your expenses and receipts. It's not polished enough to submit to the App Store, but it would have been quite useful to me personally.

I was using my app on my iPad when all of a sudden it was disabled:

!["[App] is no longer available"](/assets/no_longer_available.png){.img5}

I soon discovered that apps you install via Xcode [only last for seven days](#how-do-i-sideload-unofficially-on-ios). That didn't seem right to me. My team and I wrote the app from scratch, but it didn't really feel like "our" app, because we're not even allowed to use it on our own devices without asking Apple's cloud service for permission to do so every week into eternity. This was in stark contrast to my experience with my MacBook Pro, for which I've developed numerous utilities and apps for personal use by myself without any issue.

So, I started digging into the topic of sideloading on iOS. This website is the result of my research on the topic. It's mostly factual, but it does contain some of my opinions as well.

# 💡 Can I suggest an improvement to this website?
The source code for the website is published openly on [GitHub](https://github.com/DownrightNifty/dihsy). Since this is a personal site that contains some of my personal opinions, I'd prefer contributions that improve factual accuracy or fix errors over contributions containing your opinions. I may reject any contributions that I don't like.

# 📚 See also
Here are some essays or articles about sideloading I enjoy:

- [A Bicycle for the Mind](https://ghijklmno.net/a-bicycle-for-the-mind/) by Tom Morgan
- [Apple doesn't want you developing hobby apps](https://www.bennettnotes.com/notes/why-does-apple-restrict-hobby-development/) by Dave Bennett
- [Do you want me to leave the Apple ecosystem?](https://lapcatsoftware.com/articles/sideloading.html) by Jeff Johnson

Here are some articles or statements from digital rights advocacy groups regarding sideloading:

- [Electronic Frontier Foundation](https://www.eff.org/deeplinks/2024/10/eu-apple-let-users-choose-their-software-apple-nah)
- [Free Software Foundation Europe](https://fsfe.org/activities/apple-litigation/apple-litigation.en.html)

# 🪵 Changelog and RSS feed

<div class="PLACEHOLDER" data-id="big-rss-btn" data-label="Atom/RSS feed"></div>

[View feed in browser](/news)

I'll try to keep the website up to date as the status of sideloading and alternative app stores on iOS changes over time. The feed will be updated each time the website changes, and may also include news about sideloading and alternative app stores on iOS, or about [legislation surrounding sideloading](#which-countries-are-legislating-sideloading).

# Footnotes

[^1]: Firefox and Chrome have both decided not to port their browser engines to iOS until it becomes possible outside the EU, since it would require tremendous effort for something that the majority of users will not benefit from. See [Mozilla's statement](https://www.theverge.com/2024/1/26/24052067/mozilla-apple-ios-browser-rules-firefox) and [a Chrome engineer's statement](https://x.com/laparisa/status/1753489369095442933).

[^2]: Apple's broad interpretation of the exception provided in article 6(4) of the DMA allows them to require that all apps distributed on third party app stores be manually reviewed, approved, and signed by Apple. This may be challenged in the future by the European Commission.

[^3]: According to [Japan Times](https://www.japantimes.co.jp/business/2024/05/22/tech/smartphone-apps-competition-bill/), "\[The bill] allows designated companies to reject other app stores if there are serious concerns about security and data privacy. The Japanese government will draft guidelines for app store providers to make sure security is robust and data privacy is protected." It remains to be seen how this will be implemented and if users will be provided with an option to override the platform owner's security decisions/recommendations (provided that they accept the risks).

[^4]: The Open App Markets Act would obligate platforms to "install third-party apps or app stores through means other than its app store", but would not prevent platform owners from taking actions "necessary to achieve user privacy, security, or digital safety; taken to prevent spam or fraud; necessary to prevent unlawful infringement of preexisting intellectual property; or taken to prevent a violation of, or comply with, Federal or State law". If passed, it would be up to a court to interpret whether or not this mandates an option allowing users to override the platform owner's security decisions/recommendations (provided that they accept the risks).

[^5]: Under the court's ruling, Google is required to allow third party app stores into its Google Play Store for a period of 3 years. Critics have argued that the ruling is unnecessary because Android already allows the sideloading of third party app stores, and that Google should not be obligated to endorse and provide hosting for third party app stores inside of their privately-operated first party store. Proponents have argued that the process of sideloading is too complex for the average user to understand, and that Google unfairly disincentivizes third party app stores through "scare screens" presented to end users and business contracts with OEMs. Epic Games sued Apple at the same time as Google for similar reasons, but ultimately [lost their case](https://en.wikipedia.org/wiki/Epic_Games_v._Apple). Google has appealed the decision.

[^6]: According to the [court-issued injunction](https://storage.courtlistener.com/recap/gov.uscourts.cand.373179/gov.uscourts.cand.373179.1017.0_3.pdf), "Google is entitled to take reasonable measures to ensure that the platforms or stores, and the apps they offer, are safe from a computer systems and security standpoint, and do not offer illegal goods or services under federal or state law within the United States, or violate Google’s content standards. \[...] If challenged, Google will bear the burden of proving that its technical and content requirements and determinations are strictly necessary and narrowly tailored." It would be up to the court's technical committee, or to the court, to interpret whether or not Google can forbid app stores providing the ability to add arbitrary sources, such as F-Droid.

[^7]: For our purposes, "native apps" are apps that integrate with the OS, have direct access to native platform APIs, and can access any of the device's exposed hardware/software features, with the following caveat: if the device has a default app store, "native apps" need only the level of hardware/software access which is already available to third party apps offered through the default store.

[^8]: "Modifications you make to the system are not supported by Google, may cause hardware issues and may void warranty." Source: [Image of developer mode setup process](https://www.cnet.com/a/img/resize/97f0e8aff2aacc32107f1ab60c3ccb08b9b1ff0a/hub/2014/03/18/4de7092f-b0d3-11e3-a24e-d4ae52e62bcc/ChromeLinux-4.png?auto=webp&width=1200).

[^9]: Expected to enter into force by the end of 2025, according to [*Kyodo News*](https://english.kyodonews.net/news/2024/06/bc2d7f45d456-japan-enacts-law-to-curb-apple-googles-app-dominance.html).

[^10]: Non-commercial apps don't have to pay the CTF, but non-commercial app stores, such as AltStore PAL, still do. Despite this, AltStore PAL is currently available for free thanks to a [grant from Epic Games](https://techcrunch.com/2024/08/15/epic-games-megagrant-makes-eu-alternative-app-store-altstore-pal-available-for-free/).

[^11]: <https://www.statista.com/statistics/382260/segments-share-revenue-of-apple/>{.raw-link}

[^12]: Expected to enter into force by 8/6/2025, according to [*Mac Magazine (Portuguese)*](https://macmagazine.com.br/post/2025/05/08/justica-restabelece-medida-que-podera-mudar-a-app-store-no-brasil/).

[^13]: "Install" in the same sense as when you install any non-sideloaded app—the installation should be permanent, and the app shouldn't suddenly expire after a certain period of time, requiring an Internet connection and contact with a centralized signing service before it can be reinstalled. For example, apps sideloaded using AltStore on iOS aren't really "installed" so much as they are "temporarily loaded for testing/debugging purposes".

[^14]: Google has appealed the decision, and was granted a temporary stay on the injunction until the appeal is processed. Source: [*The Verge*](https://www.theverge.com/2024/10/18/24271996/google-epic-lawsuit-play-third-party-app-store-changes-delayed-administrative-stay-granted).
