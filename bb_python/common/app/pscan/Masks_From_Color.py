<!DOCTYPE html>
<html lang="en" dir="ltr" class="client-nojs">
<head>
<meta charset="UTF-8" />
<title>Masks From Color.py - Agisoft</title>
<meta name="generator" content="MediaWiki 1.24.1" />
<link rel="shortcut icon" href="/favicon.ico" />
<link rel="search" type="application/opensearchdescription+xml" href="/w/opensearch_desc.php" title="Agisoft (en)" />
<link rel="EditURI" type="application/rsd+xml" href="http://wiki.agisoft.com/w/api.php?action=rsd" />
<link rel="alternate" hreflang="x-default" href="/wiki/Masks_From_Color.py" />
<link rel="alternate" type="application/atom+xml" title="Agisoft Atom feed" href="/w/index.php?title=Special:RecentChanges&amp;feed=atom" />
<link rel="stylesheet" href="http://wiki.agisoft.com/w/load.php?debug=false&amp;lang=en&amp;modules=mediawiki.legacy.commonPrint%2Cshared%7Cmediawiki.skinning.interface%7Cmediawiki.ui.button%7Cskins.vector.styles&amp;only=styles&amp;skin=vector&amp;*" />
<meta name="ResourceLoaderDynamicStyles" content="" />
<style>a:lang(ar),a:lang(kk-arab),a:lang(mzn),a:lang(ps),a:lang(ur){text-decoration:none}
/* cache key: db1042778_wiki:resourceloader:filter:minify-css:7:82a81660b69ce378658bf6344ae2f5fa */</style>
<script src="http://wiki.agisoft.com/w/load.php?debug=false&amp;lang=en&amp;modules=startup&amp;only=scripts&amp;skin=vector&amp;*"></script>
<script>if(window.mw){
mw.config.set({"wgCanonicalNamespace":"","wgCanonicalSpecialPageName":false,"wgNamespaceNumber":0,"wgPageName":"Masks_From_Color.py","wgTitle":"Masks From Color.py","wgCurRevisionId":101,"wgRevisionId":101,"wgArticleId":71,"wgIsArticle":true,"wgIsRedirect":false,"wgAction":"view","wgUserName":null,"wgUserGroups":["*"],"wgCategories":[],"wgBreakFrames":false,"wgPageContentLanguage":"en","wgPageContentModel":"wikitext","wgSeparatorTransformTable":["",""],"wgDigitTransformTable":["",""],"wgDefaultDateFormat":"dmy","wgMonthNames":["","January","February","March","April","May","June","July","August","September","October","November","December"],"wgMonthNamesShort":["","Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"],"wgRelevantPageName":"Masks_From_Color.py","wgIsProbablyEditable":false,"wgRestrictionEdit":[],"wgRestrictionMove":[]});
}</script><script>if(window.mw){
mw.loader.implement("user.options",function($,jQuery){mw.user.options.set({"ccmeonemails":0,"cols":80,"date":"default","diffonly":0,"disablemail":0,"editfont":"default","editondblclick":0,"editsectiononrightclick":0,"enotifminoredits":0,"enotifrevealaddr":0,"enotifusertalkpages":1,"enotifwatchlistpages":1,"extendwatchlist":0,"fancysig":0,"forceeditsummary":0,"gender":"unknown","hideminor":0,"hidepatrolled":0,"imagesize":2,"math":1,"minordefault":0,"newpageshidepatrolled":0,"nickname":"","norollbackdiff":0,"numberheadings":0,"previewonfirst":0,"previewontop":1,"rcdays":7,"rclimit":50,"rows":25,"showhiddencats":0,"shownumberswatching":1,"showtoolbar":1,"skin":"vector","stubthreshold":0,"thumbsize":5,"underline":2,"uselivepreview":0,"usenewrc":0,"watchcreations":1,"watchdefault":1,"watchdeletion":0,"watchlistdays":3,"watchlisthideanons":0,"watchlisthidebots":0,"watchlisthideliu":0,"watchlisthideminor":0,"watchlisthideown":0,"watchlisthidepatrolled":0,"watchmoves":0,"watchrollback":0,
"wllimit":250,"useeditwarning":1,"prefershttps":1,"language":"en","variant-gan":"gan","variant-iu":"iu","variant-kk":"kk","variant-ku":"ku","variant-shi":"shi","variant-sr":"sr","variant-tg":"tg","variant-uz":"uz","variant-zh":"zh","searchNs0":true,"searchNs1":false,"searchNs2":false,"searchNs3":false,"searchNs4":false,"searchNs5":false,"searchNs6":false,"searchNs7":false,"searchNs8":false,"searchNs9":false,"searchNs10":false,"searchNs11":false,"searchNs12":false,"searchNs13":false,"searchNs14":false,"searchNs15":false,"variant":"en"});},{},{});mw.loader.implement("user.tokens",function($,jQuery){mw.user.tokens.set({"editToken":"+\\","patrolToken":"+\\","watchToken":"+\\"});},{},{});
/* cache key: db1042778_wiki:resourceloader:filter:minify-js:7:2ffb09fddb30ef53a64cefb237597916 */
}</script>
<script>if(window.mw){
mw.loader.load(["mediawiki.page.startup","mediawiki.legacy.wikibits","mediawiki.legacy.ajax","skins.vector.js"]);
}</script>
<!--[if lt IE 7]><style type="text/css">body{behavior:url("/w/skins/Vector/csshover.min.htc")}</style><![endif]-->
</head>
<body class="mediawiki ltr sitedir-ltr ns-0 ns-subject page-Masks_From_Color_py skin-vector action-view vector-animateLayout">
		<div id="mw-page-base" class="noprint"></div>
		<div id="mw-head-base" class="noprint"></div>
		<div id="content" class="mw-body" role="main">
			<a id="top"></a>

						<h1 id="firstHeading" class="firstHeading" lang="en"><span dir="auto">Masks From Color.py</span></h1>
						<div id="bodyContent" class="mw-body-content">
									<div id="siteSub">From Agisoft</div>
								<div id="contentSub"></div>
												<div id="jump-to-nav" class="mw-jump">
					Jump to:					<a href="#mw-navigation">navigation</a>, 					<a href="#p-search">search</a>
				</div>
				<div id="mw-content-text" lang="en" dir="ltr" class="mw-content-ltr"><pre>
#creates masks for cameras in the active chunk, based on user defined color and tolerance

#compatibility PhotoScan Pro 1.1.0

import PhotoScan
from PySide import QtGui, QtCore

class MaskByColor(QtGui.QDialog):

	def __init__(self, parent):
	
		QtGui.QDialog.__init__(self, parent)
		
		self.color = QtGui.QColor(0, 0, 0)
		red, green, blue = self.color.red(), self.color.green(), self.color.blue()

		self.setWindowTitle(&quot;Masking by color:&quot;)
		
		self.btnQuit = QtGui.QPushButton(&quot;Quit&quot;)
		self.btnQuit.setFixedSize(100,50)
		
		self.btnP1 = QtGui.QPushButton(&quot;Mask&quot;)
		self.btnP1.setFixedSize(100,50)
		
		self.pBar = QtGui.QProgressBar()
		self.pBar.setTextVisible(False)
		self.pBar.setFixedSize(130, 50)
		
		self.selTxt = QtGui.QLabel()
		self.selTxt.setText(&quot;Apply to:&quot;)
		self.selTxt.setFixedSize(100, 25)	
		
		self.radioBtn_all = QtGui.QRadioButton(&quot;all cameras&quot;)
		self.radioBtn_sel = QtGui.QRadioButton(&quot;selected cameras&quot;)
		self.radioBtn_all.setChecked(True)
		self.radioBtn_sel.setChecked(False)
		
		self.colTxt = QtGui.QLabel()
		self.colTxt.setText(&quot;Select color:&quot;)
		self.colTxt.setFixedSize(100, 25)	
		
		strColor = &quot;{:0&gt;2d}{:0&gt;2d}{:0&gt;2d}&quot;.format(int(hex(red)[2:]), int(hex(green)[2:]), int(hex(blue)[2:])) 
		self.btnCol = QtGui.QPushButton(strColor)
		self.btnCol.setFixedSize(80, 25)	
		pix = QtGui.QPixmap(10, 10)
		pix.fill(self.color)
		icon = QtGui.QIcon()
		icon.addPixmap(pix)
		self.btnCol.setIcon(icon)
		palette = QtGui.QPalette()
		palette.setColor(QtGui.QPalette.Button, self.color)
		self.btnCol.setPalette(palette)
		self.btnCol.setAutoFillBackground(True)
		
		self.txtTol = QtGui.QLabel()
		self.txtTol.setText(&quot;Tolerance:&quot;)
		self.txtTol.setFixedSize(100, 25)	
		
		self.sldTol = QtGui.QSlider()
		self.sldTol.setOrientation(QtCore.Qt.Orientation.Horizontal)
		self.sldTol.setMinimum(0)
		self.sldTol.setMaximum(99)
		
		hbox = QtGui.QHBoxLayout()
		hbox.addStretch(1)
		hbox.addWidget(self.pBar)
		hbox.addWidget(self.btnP1)
		hbox.addWidget(self.btnQuit)		
		
		layout = QtGui.QGridLayout()   
		layout.setSpacing(5)
		layout.addWidget(self.selTxt, 0, 0)
		layout.addWidget(self.radioBtn_all, 1, 0)
		layout.addWidget(self.radioBtn_sel, 2, 0)
		layout.addWidget(self.colTxt, 0, 1)
		layout.addWidget(self.btnCol, 1, 1)
		layout.addWidget(self.txtTol, 0, 2)
		layout.addWidget(self.sldTol, 1, 2)
		layout.addLayout(hbox, 3, 0, 5, 3)
		self.setLayout(layout)  		
		
		proc_mask = lambda&#160;: self.maskColor()
		proc_color = lambda&#160;: self.changeColor()
		
		QtCore.QObject.connect(self.btnP1, QtCore.SIGNAL(&quot;clicked()&quot;), proc_mask)
		QtCore.QObject.connect(self.btnCol, QtCore.SIGNAL(&quot;clicked()&quot;), proc_color)
		QtCore.QObject.connect(self.btnQuit, QtCore.SIGNAL(&quot;clicked()&quot;), self, QtCore.SLOT(&quot;reject()&quot;))	

		self.exec()
		
	def changeColor (self):
	
		color = QtGui.QColorDialog.getColor()
	
		self.color = color
		red, green, blue = color.red(), color.green(), color.blue()	
		if red &lt; 16:
			red = &quot;0&quot; + hex(red)[2:]
		else:
			red = hex(red)[2:]
		if green &lt; 16:
			green = &quot;0&quot; + hex(green)[2:]
		else:
			green = hex(green)[2:]
		if blue &lt; 16:
			blue = &quot;0&quot; + hex(blue)[2:]
		else:
			blue = hex(blue)[2:]
		
		strColor = red + green + blue
		self.btnCol.setText(strColor)
		
		pix = QtGui.QPixmap(10, 10)
		pix.fill(self.color)
		icon = QtGui.QIcon()
		icon.addPixmap(pix)
		self.btnCol.setIcon(icon)
		
		palette = self.btnCol.palette()
		palette.setColor(QtGui.QPalette.Button, self.color)
		self.btnCol.setPalette(palette)
		self.btnCol.setAutoFillBackground(True)
		
		return True

	def maskColor (self):
	
		tolerance = 10
		tolerance = self.sldTol.value()
		
		self.sldTol.setDisabled(True)
		self.btnCol.setDisabled(True)
		self.btnP1.setDisabled(True)
		self.btnQuit.setDisabled(True)
	
		chunk = PhotoScan.app.document.chunk
		mask_list = list()
		if self.radioBtn_sel.isChecked():
			for photo in chunk.cameras:
				if photo.selected:
					mask_list.append(photo)
		elif self.radioBtn_all.isChecked():
			mask_list = list(chunk.cameras)
			
		if not len(mask_list):
			PhotoScan.app.messageBox(&quot;Nothing to mask!&quot;)
			return False

		color = self.color
		red, green, blue = color.red(), color.green(), color.blue()

		processed = 0
		
		for camera in mask_list:
			for frame in camera.frames:
				QtGui.qApp.processEvents()
				mask = PhotoScan.utils.createDifferenceMask(frame.photo.image(), (red, green, blue), tolerance, False)
				m = PhotoScan.Mask()
				m.setImage(mask)
				frame.mask = m
				processed += 1
				self.pBar.setValue(int(processed / len(mask_list) / len(chunk.frames) * 100))
				
			
		print(&quot;Masking finished. &quot; + str(processed) + &quot; images masked.\n&quot;)
		
		self.sldTol.setDisabled(False)
		self.btnCol.setDisabled(False)
		self.btnP1.setDisabled(False)
		self.btnQuit.setDisabled(False)
		
		return True		
		
def main():

	global doc
	doc = PhotoScan.app.document

	app = QtGui.QApplication.instance()
	parent = app.activeWindow()
	
	dlg = MaskByColor(parent)
		
		
PhotoScan.app.addMenuItem(&quot;Custom/Masking by color&quot;, main)
</pre>

<!-- 
NewPP limit report
CPU time usage: 0.008 seconds
Real time usage: 0.009 seconds
Preprocessor visited node count: 4/1000000
Preprocessor generated node count: 24/1000000
Post‐expand include size: 0/2097152 bytes
Template argument size: 0/2097152 bytes
Highest expansion depth: 2/40
Expensive parser function count: 0/100
-->

<!-- Saved in parser cache with key db1042778_wiki:pcache:idhash:71-0!*!*!*!*!*!* and timestamp 20150323153732 and revision id 101
 -->
</div>									<div class="printfooter">
						Retrieved from "<a dir="ltr" href="http://wiki.agisoft.com/w/index.php?title=Masks_From_Color.py&amp;oldid=101">http://wiki.agisoft.com/w/index.php?title=Masks_From_Color.py&amp;oldid=101</a>"					</div>
													<div id='catlinks' class='catlinks catlinks-allhidden'></div>												<div class="visualClear"></div>
							</div>
		</div>
		<div id="mw-navigation">
			<h2>Navigation menu</h2>

			<div id="mw-head">
									<div id="p-personal" role="navigation" class="" aria-labelledby="p-personal-label">
						<h3 id="p-personal-label">Personal tools</h3>
						<ul>
							<li id="pt-login"><a href="/w/index.php?title=Special:UserLogin&amp;returnto=Masks+From+Color.py" title="You are encouraged to log in; however, it is not mandatory [o]" accesskey="o">Log in</a></li><li id="pt-createaccount"><a href="/wiki/Special:RequestAccount">Request account</a></li>						</ul>
					</div>
									<div id="left-navigation">
										<div id="p-namespaces" role="navigation" class="vectorTabs" aria-labelledby="p-namespaces-label">
						<h3 id="p-namespaces-label">Namespaces</h3>
						<ul>
															<li  id="ca-nstab-main" class="selected"><span><a href="/wiki/Masks_From_Color.py"  title="View the content page [c]" accesskey="c">Page</a></span></li>
															<li  id="ca-talk" class="new"><span><a href="/w/index.php?title=Talk:Masks_From_Color.py&amp;action=edit&amp;redlink=1"  title="Discussion about the content page [t]" accesskey="t">Discussion</a></span></li>
													</ul>
					</div>
										<div id="p-variants" role="navigation" class="vectorMenu emptyPortlet" aria-labelledby="p-variants-label">
												<h3 id="p-variants-label"><span>Variants</span><a href="#"></a></h3>

						<div class="menu">
							<ul>
															</ul>
						</div>
					</div>
									</div>
				<div id="right-navigation">
										<div id="p-views" role="navigation" class="vectorTabs" aria-labelledby="p-views-label">
						<h3 id="p-views-label">Views</h3>
						<ul>
															<li id="ca-view" class="selected"><span><a href="/wiki/Masks_From_Color.py" >Read</a></span></li>
															<li id="ca-viewsource"><span><a href="/w/index.php?title=Masks_From_Color.py&amp;action=edit"  title="This page is protected.&#10;You can view its source [e]" accesskey="e">View source</a></span></li>
															<li id="ca-history" class="collapsible"><span><a href="/w/index.php?title=Masks_From_Color.py&amp;action=history"  title="Past revisions of this page [h]" accesskey="h">View history</a></span></li>
													</ul>
					</div>
										<div id="p-cactions" role="navigation" class="vectorMenu emptyPortlet" aria-labelledby="p-cactions-label">
						<h3 id="p-cactions-label"><span>More</span><a href="#"></a></h3>

						<div class="menu">
							<ul>
															</ul>
						</div>
					</div>
										<div id="p-search" role="search">
						<h3>
							<label for="searchInput">Search</label>
						</h3>

						<form action="/w/index.php" id="searchform">
														<div id="simpleSearch">
															<input type="search" name="search" placeholder="Search" title="Search Agisoft [f]" accesskey="f" id="searchInput" /><input type="hidden" value="Special:Search" name="title" /><input type="submit" name="fulltext" value="Search" title="Search the pages for this text" id="mw-searchButton" class="searchButton mw-fallbackSearchButton" /><input type="submit" name="go" value="Go" title="Go to a page with this exact name if exists" id="searchButton" class="searchButton" />								</div>
						</form>
					</div>
									</div>
			</div>
			<div id="mw-panel">
				<div id="p-logo" role="banner"><a style="background-image: url(/w/resources/assets/photoscan.png);" href="/wiki/Main_Page"  title="Visit the main page"></a></div>
						<div class="portal" role="navigation" id='p-navigation' aria-labelledby='p-navigation-label'>
			<h3 id='p-navigation-label'>Navigation</h3>

			<div class="body">
									<ul>
													<li id="n-mainpage-description"><a href="/wiki/Main_Page" title="Visit the main page [z]" accesskey="z">Main page</a></li>
													<li id="n-recentchanges"><a href="/wiki/Special:RecentChanges" title="A list of recent changes in the wiki [r]" accesskey="r">Recent changes</a></li>
													<li id="n-randompage"><a href="/wiki/Special:Random" title="Load a random page [x]" accesskey="x">Random page</a></li>
													<li id="n-help"><a href="https://www.mediawiki.org/wiki/Special:MyLanguage/Help:Contents" title="The place to find out">Help</a></li>
											</ul>
							</div>
		</div>
			<div class="portal" role="navigation" id='p-tb' aria-labelledby='p-tb-label'>
			<h3 id='p-tb-label'>Tools</h3>

			<div class="body">
									<ul>
													<li id="t-whatlinkshere"><a href="/wiki/Special:WhatLinksHere/Masks_From_Color.py" title="A list of all wiki pages that link here [j]" accesskey="j">What links here</a></li>
													<li id="t-recentchangeslinked"><a href="/wiki/Special:RecentChangesLinked/Masks_From_Color.py" title="Recent changes in pages linked from this page [k]" accesskey="k">Related changes</a></li>
													<li id="t-specialpages"><a href="/wiki/Special:SpecialPages" title="A list of all special pages [q]" accesskey="q">Special pages</a></li>
													<li id="t-print"><a href="/w/index.php?title=Masks_From_Color.py&amp;printable=yes" rel="alternate" title="Printable version of this page [p]" accesskey="p">Printable version</a></li>
													<li id="t-permalink"><a href="/w/index.php?title=Masks_From_Color.py&amp;oldid=101" title="Permanent link to this revision of the page">Permanent link</a></li>
													<li id="t-info"><a href="/w/index.php?title=Masks_From_Color.py&amp;action=info">Page information</a></li>
											</ul>
							</div>
		</div>
				</div>
		</div>
		<div id="footer" role="contentinfo">
							<ul id="footer-info">
											<li id="footer-info-lastmod"> This page was last modified on 6 February 2015, at 15:16.</li>
											<li id="footer-info-viewcount">This page has been accessed 140 times.</li>
									</ul>
							<ul id="footer-places">
											<li id="footer-places-privacy"><a href="/wiki/Agisoft:Privacy_policy" title="Agisoft:Privacy policy">Privacy policy</a></li>
											<li id="footer-places-about"><a href="/wiki/Agisoft:About" title="Agisoft:About">About Agisoft</a></li>
											<li id="footer-places-disclaimer"><a href="/wiki/Agisoft:General_disclaimer" title="Agisoft:General disclaimer">Disclaimers</a></li>
									</ul>
										<ul id="footer-icons" class="noprint">
											<li id="footer-poweredbyico">
															<a href="//www.mediawiki.org/"><img src="/w/resources/assets/poweredby_mediawiki_88x31.png" alt="Powered by MediaWiki" width="88" height="31" /></a>
													</li>
									</ul>
						<div style="clear:both"></div>
		</div>
		<script>/*<![CDATA[*/window.jQuery && jQuery.ready();/*]]>*/</script><script>if(window.mw){
mw.loader.state({"site":"ready","user":"ready","user.groups":"ready"});
}</script>
<script>if(window.mw){
mw.loader.load(["mediawiki.action.view.postEdit","mediawiki.user","mediawiki.hidpi","mediawiki.page.ready","mediawiki.searchSuggest"],null,true);
}</script>
<script>if(window.mw){
mw.config.set({"wgBackendResponseTime":546});
}</script>
	</body>
</html>
	